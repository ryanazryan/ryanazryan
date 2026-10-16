"""Read GitHub's public calendar and rebuild a truthful, dated local snapshot.
No token, write access, Git operation or deployment. Python 3.10+.
"""
import argparse, json, re, urllib.request
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime, timezone, timedelta, date

ROOT = Path(__file__).resolve().parents[1]
class Calendar(HTMLParser):
    def __init__(self):
        super().__init__(); self.days={}; self.tips={}; self.tip=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if a.get('data-date') and a.get('data-level') is not None:
            self.days[a['id']]={'date':a['data-date'],'level':int(a['data-level'])}
        if tag=='tool-tip' and a.get('for'):
            self.tip=a['for']; self.tips[self.tip]=''
    def handle_data(self, data):
        if self.tip:self.tips[self.tip]+=data
    def handle_endtag(self, tag):
        if tag=='tool-tip':self.tip=None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--through',default=datetime.now(timezone(timedelta(hours=8))).date().isoformat());ap.add_argument('--input',type=Path);args=ap.parse_args()
    through=date.fromisoformat(args.through);start=date(through.year,1,1)
    url=f'https://github.com/users/ryanazryan/contributions?from={start}&to={through}'
    if args.input:html=args.input.read_text(encoding='utf-8')
    else:
        req=urllib.request.Request(url,headers={'User-Agent':'Ryan-Studio-Calendar/1.0'})
        with urllib.request.urlopen(req,timeout=30) as response:html=response.read().decode('utf-8')
    parser=Calendar();parser.feed(html);days=[]
    for id,item in parser.days.items():
        if not str(start)<=item['date']<=str(through):continue
        tip=parser.tips.get(id,'').strip();match=re.search(r'([\d,]+) contributions?',tip)
        if tip.startswith('No contributions'):count=0
        elif match:count=int(match.group(1).replace(',',''))
        else:raise ValueError(f'Cannot verify count for {item["date"]}; existing snapshot left unchanged.')
        if not 0<=item['level']<=4:raise ValueError('Unexpected intensity level')
        days.append({**item,'count':count})
    days.sort(key=lambda d:d['date'])
    if len(days)!=(through-start).days+1 or len({d['date'] for d in days})!=len(days):raise ValueError('Incomplete calendar; existing snapshot left unchanged.')
    data={'username':'ryanazryan','source':url,'checked_on':str(through),'range_start':str(start),'range_end':str(through),'total':sum(d['count'] for d in days),'days':days,'note':'Publicly visible GitHub calendar. Counts follow GitHub visibility rules. Heights encode GitHub intensity level 0–4, not exact count. This is a dated snapshot, not a live counter.'}
    dest=ROOT/'design/contributions.json';dest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(f'Validated {len(days)} days, {data["total"]} contributions; saved {dest.name}.')
    print('Now run: python design/build-assets.py --activity-only')
if __name__=='__main__':main()
