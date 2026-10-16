"""Editable design source. Rebuild outlined SVGs with: pip install fonttools
Then: python design/build-assets.py. Art inputs live in design/renders.
Fonts are OFL licensed and bundled in docs/fonts. No installed font dependency.
Use --editable to emit SVGs with editable text into design/editable (not README).
"""
import argparse, base64, html, json, math, calendar
from pathlib import Path
from datetime import date, timedelta
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT=Path(__file__).resolve().parents[1]
ARGS=argparse.ArgumentParser();ARGS.add_argument('--editable',action='store_true');ARGS.add_argument('--activity-only',action='store_true');args=ARGS.parse_args()
OUT=ROOT/('design/editable' if args.editable else 'assets');OUT.mkdir(exist_ok=True,parents=True)
C={'ink':'#202624','ivory':'#f3efe6','sage':'#8fa99b','green':'#405f54','amber':'#d2a875','stone':'#b9b6ac','muted':'#5c6b61'}
FONTS={}
for name,weight in [('SpaceGrotesk',500),('Manrope',450),('Silkscreen',400)]:
    f=TTFont(ROOT/f'docs/fonts/{name}.ttf')
    if 'fvar' in f:f=instantiateVariableFont(f,{'wght':weight},inplace=True)
    FONTS[name]=f

def text(s,x,y,size=24,color=C['ink'],font='SpaceGrotesk',tracking=0):
    if args.editable:return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" letter-spacing="{tracking}" fill="{color}">{html.escape(s)}</text>'
    f=FONTS[font];glyphs=f.getGlyphSet();cmap=f.getBestCmap();scale=size/f['head'].unitsPerEm;pen=SVGPathPen(glyphs,ntos=lambda v:format(v,'.2f').rstrip('0').rstrip('.') if v else '0');cursor=x
    for char in s:
        if ord(char) not in cmap:raise ValueError(f'Unsupported character {char!r} in {font}')
        name=cmap.get(ord(char),'space');glyphs[name].draw(TransformPen(pen,(scale,0,0,-scale,cursor,y)));cursor+=f['hmtx'][name][0]*scale+tracking
    return f'<path fill="{color}" d="{pen.getCommands()}"/>'
def rect(x,y,w,h,c,r=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'
def line(x,y,x2,y2,c,w=1):return f'<path d="M{x} {y}L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{w}"/>'
def circle(x,y,r,c):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
def raster(name,x,y,w,h):
    p=ROOT/f'design/renders/{name}.jpg';mime='jpeg'
    if name=='game-room':p=ROOT/'design/renders/game-room.png';mime='png'
    pixel=' style="image-rendering:pixelated"' if name=='game-room' else ''
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}" preserveAspectRatio="xMidYMid meet"{pixel}/>'
def svg(name,w,h,body,title,desc,bg=None):
    root=f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>'
    (OUT/f'{name}.svg').write_text(root+(rect(0,0,w,h,bg) if bg else '')+body+'</svg>',encoding='utf-8')

def hero(mobile=False):
    if mobile:
        b=text('Ryan.',36,139,116,tracking=-6)+text('Creative Engineering Studio',40,181,23)+line(40,205,560,205,'#c5c8b8')
        b+=text('Software Engineer &',40,250,27)+text('Full-Stack Developer',40,283,27,C['green'])+text('Informatics Student · AI Enthusiast',40,320,21,font='Manrope')
        b+=raster('hero',0,348,600,400)+text('A thoughtful place to build.',40,786,23)+text('Naufal Faiq Azryan · Indonesia',40,817,20,font='Manrope')
        svg('hero-mobile',600,850,b,"Ryan's Creative Engineering Studio",'Ryan. Software Engineer & Full-Stack Developer. Informatics Student · AI Enthusiast. Naufal Faiq Azryan, Indonesia. Original 3D-style architectural studio illustration.',C['ivory']);return
    b=raster('hero',402,26,798,532)+text('Ryan.',54,202,150,tracking=-8)
    b+=text('Creative Engineering',60,252,25)+text('Studio',60,285,25)+line(60,317,351,317,'#bec5b5')
    b+=text('Software Engineer &',60,363,25)+text('Full-Stack Developer',60,396,25,C['green'])
    b+=text('Informatics Student',60,440,17,font='Manrope')+text('AI Enthusiast · Indonesia',60,467,17,font='Manrope')
    b+=line(60,574,1140,574,'#c5c8b8')+text('A thoughtful place to build.',60,620,29)+text('Naufal Faiq Azryan',855,619,22,C['muted'])
    # SVG-native, reduced-motion-aware detail. Still frame remains complete.
    b+='<defs><radialGradient id="lamp"><stop stop-color="#f7d99c" stop-opacity=".6"/><stop offset="1" stop-color="#f7d99c" stop-opacity="0"/></radialGradient></defs><style>@keyframes breathe{0%,100%{opacity:.25}50%{opacity:.6}}.light{animation:breathe 6s ease-in-out infinite}@media(prefers-reduced-motion:reduce){.light{animation:none;opacity:.25}}</style><circle class="light" cx="627" cy="218" r="31" opacity=".25" fill="url(#lamp)"/>'
    svg('hero',1200,670,b,"Ryan's Creative Engineering Studio",'Ryan. Software Engineer & Full-Stack Developer. Informatics Student · AI Enthusiast, Indonesia. A warm miniature studio with an oak desk, editor, task lamp, books, plants and server. Original AI-generated concept artwork, not an application screenshot.',C['ivory'])

PROJECTS=[
('auvrion','01','Auvrion Biosphere','Environmental intelligence','Biodiversity, fire-risk monitoring & WebGIS.','Foundations in progress','Next.js · TypeScript · PostgreSQL / PostGIS'),
('ruma','02','Ruma Marketplace','Commerce, thoughtfully planned','Workspace and architecture groundwork.','Early setup · application not yet implemented','Planned: Next.js · NestJS · PostgreSQL'),
('hydropedia','03','Hydropedia','A little closer to growing things','Academic plant management & monitoring.','Academic team project','Java · Spring Boot · Thymeleaf · SQLite'),
('sena','04','SENA Education','Room to read. Room to grow.','Literacy learning with student & teacher views.','Learning-platform project','React · TypeScript · Vite · Firebase')]
def project(row,mobile=False):
    key,num,name,headline,summary,status,stack=row
    if mobile:
        b=raster(key,0,0,600,400)+text(num+' / Selected work',32,433,21,C['green'],font='Manrope')+text(name,32,483,36,tracking=-1)+text(headline,32,523,26)
        b+=text(summary,32,559,22,font='Manrope')+text(status,32,599,21,C['green'],font='Manrope')+line(32,622,568,622,'#c5c8b8')+text(stack,32,655,21,font='Manrope')
        svg(f'project-{key}-mobile',600,688,b,name,f'{headline}. {summary} {status}. {stack}. Concept illustration; not a product screenshot.',C['ivory']);return
    b=raster(key,600,0,600,400)+text(num+' / Selected work',48,54,17,C['green'],font='Manrope')
    b+=text(name,48,126,45,tracking=-1.4)+text(headline,48,173,24)+text(summary,48,212,19,font='Manrope')
    b+=circle(53,261,4,C['green'])+text(status,66,268,17,C['green'],font='Manrope')
    b+=line(48,304,560,304,'#c5c8b8')+text(stack,48,340,17,font='Manrope')+text('Explore the repository',48,374,17,C['green'],font='Manrope')+f'<path d="M251 374l10-10m-10 0h10v10" stroke="#405f54" stroke-width="1.5" fill="none"/>'
    svg(f'project-{key}',1200,400,b,name,f'{headline}. {summary} {status}. {stack}. Original concept illustration; not a screenshot.',C['ivory'])

def achievements():
    b=text('Small milestones, kept with care.',48,64,35,C['ivory'],tracking=-1)
    names=['Pull Shark','Pair Extraordinaire','YOLO','Quickdraw'];sub=['x2 on GitHub','Earned','Earned','Earned']
    for i,name in enumerate(names):
        x=54+i*286
        b+=rect(x+4,250,236,15,'#17201b',3)+rect(x,239,240,12,'#a18057',2)+rect(x+20,218,200,22,'#405249',3)
        # Original little metal sculptures, deliberately distinct from GitHub badges.
        if i==0:
            b+=f'<path d="M{x+72} 205L{x+125} 119L{x+166} 205Z" fill="#8fa99b"/><path d="M{x+125} 119L{x+132} 199L{x+166} 205Z" fill="#607e6e"/>'+rect(x+56,202,130,8,'#d2a875',2)
        elif i==1:
            b+=circle(x+99,157,30,'#d2a875')+circle(x+143,178,30,'#8fa99b')+circle(x+99,157,18,'#202624')+circle(x+143,178,18,'#202624')+line(x+110,173,x+132,162,'#eee4cc',8)
        elif i==2:
            b+=f'<path d="M{x+130} 116L{x+83} 173H{x+116}L{x+103} 208L{x+161} 153H{x+127}Z" fill="#d2a875"/>'
        else:
            b+=circle(x+120,166,42,'#8fa99b')+circle(x+120,166,33,'#35483e')+line(x+120,166,x+137,141,'#e7c89a',5)+line(x+120,166,x+102,166,'#e7c89a',4)+rect(x+109,115,22,7,'#d2a875',2)
        b+=text(name,x+12,290,22,C['ivory'])+text(sub[i],x+12,319,16,'#b5c6b5',font='Manrope')
    b+=text('Original, unofficial studio sculptures · achievements verified on 16 Oct 2026',48,371,17,'#b5c6b5',font='Manrope')
    svg('achievements',1200,407,b,'Achievements & Engineering Activity','Verified on 16 October 2026: Pull Shark x2, Pair Extraordinaire, YOLO and Quickdraw. Original unofficial artwork; open GitHub to see the official achievement badges.',C['ink'])
    # Reflow the actual sculptures into two columns for narrow README screens.
    # Standard-library XML is enough; no browser fonts are used.
    import xml.etree.ElementTree as ET
    root=ET.fromstring((OUT/'achievements.svg').read_text(encoding='utf-8'))
    children=list(root);mobile=text('Small milestones,',32,53,30,C['ivory'])+text('kept with care.',32,90,30,C['ivory'])
    # Extract sculpture groups by their explicit source construction below.
    for i in range(4):
        x=54+i*286;mx=14+(i%2)*290;my=(i//2)*258
        fragment='';in_group=False
        for element in children:
            tag=element.tag.split('}')[-1]
            if tag=='rect' and element.get('x')==str(x+4) and element.get('y')=='250':in_group=True
            if in_group:
                if tag=='rect' and element.get('x')==str(x+4+286) and element.get('y')=='250':break
                # Footer begins after the last group's label; skip its path.
                if i==3 and element is children[-1]:break
                fragment+=ET.tostring(element,encoding='unicode')
        mobile+=f'<g transform="translate({mx-x}, {my})">{fragment}</g>'
    mobile+=text('Unofficial artwork · verified 16 Oct 2026',32,638,17,'#b5c6b5',font='Manrope')
    svg('achievements-mobile',600,675,mobile,'Verified GitHub achievement shelf','Pull Shark x2, Pair Extraordinaire, YOLO and Quickdraw. Original unofficial studio sculptures. Verified 16 October 2026.',C['ink'])

def activity():
    data=json.loads((ROOT/'design/contributions.json').read_text());days=data['days'];total=data['total'];active=sum(d['count']>0 for d in days)
    b=text('A garden of small contributions.',48,63,35,tracking=-1)+text(f'{total} contributions',48,109,25,C['green'])+text(f'{active} active days · {data["range_start"]} to {data["range_end"]}',360,109,18,font='Manrope')
    start=date.fromisoformat(days[0]['date']);start-=timedelta(days=(start.weekday()+1)%7)
    colors=['#e3e5d9','#afc1a8','#8fa99b','#668b75','#405f54']
    for d in days:
        delta=(date.fromisoformat(d['date'])-start).days;week=delta//7;dow=delta%7;x=65+week*21+dow*13;y=164+dow*12;h=2+d['level']*6
        top=f'{x},{y-h} {x+17},{y-h} {x+27},{y+8-h} {x+10},{y+8-h}'
        b+=f'<g><title>{d["date"]}: {d["count"]} contributions</title><path d="M{x+10} {y+8-h}h17v{h}h-17Z" fill="#a6b29d"/><path d="M{x} {y-h}l10 8v{h}l-10 -8Z" fill="#bdc7b3"/><polygon points="{top}" fill="{colors[d["level"]]}"/></g>'
    b+=text('Jan',66,283,16,font='Manrope')+text('Apr',339,283,16,font='Manrope')+text('Jul',612,283,16,font='Manrope')+text('Oct',885,283,16,font='Manrope')
    b+=text('Public GitHub calendar · dated snapshot, not a live counter',48,334,17,C['muted'],font='Manrope')
    for i,col in enumerate(colors):b+=rect(924+i*27,318,20,16,col,2)
    b+=text('Less',873,333,13,C['muted'],font='Manrope')+text('More',1067,333,13,C['muted'],font='Manrope')
    svg('contributions',1200,369,b,'GitHub contribution garden',f'ryanazryan: {total} publicly visible contributions across {active} active days from {data["range_start"]} to {data["range_end"]}. Snapshot checked on {data["checked_on"]}. Column heights show GitHub intensity levels, not counts. See the linked GitHub calendar for current activity.',C['ivory'])
    readme=ROOT/'README.md'
    if readme.exists() and not args.editable:
        content=readme.read_text(encoding='utf-8');begin='<!-- activity:start -->';end='<!-- activity:end -->'
        if begin in content and end in content:
            d0=date.fromisoformat(data['range_start']);d1=date.fromisoformat(data['range_end']);period=f'{d0.day} {calendar.month_name[d0.month]} to {d1.day} {calendar.month_name[d1.month]} {d1.year}'
            block=f'''{begin}
<a href="https://github.com/ryanazryan?tab=overview&amp;from={d0}&amp;to={d1}">
  <img src="assets/contributions.svg" width="100%" alt="Ryan's contribution garden. {total} publicly visible GitHub contributions across {active} active days, {period}. A dated snapshot; column heights represent GitHub intensity levels.">
</a>

**{total} contributions · {active} active days** in the public calendar from {period}. [Current activity on GitHub ↗](https://github.com/ryanazryan)

<sub>Local artwork with a [verifiable data snapshot](design/contributions.json). No live counter, streak promise, or external image service.</sub>
{end}'''
            a=content.index(begin);z=content.index(end,a)+len(end);readme.write_text(content[:a]+block+content[z:],encoding='utf-8')

def toolkit(mobile=False):
    groups=[('Languages',['TypeScript · JavaScript · Go','PHP · Python · Java · Dart']),('Frontend',['React · Next.js','Tailwind CSS · Bootstrap']),('Backend',['Node.js · Laravel','Spring Boot']),('Data & cloud',['PostgreSQL · MySQL','Firebase · Vercel']),('Developer tools',['Git · GitHub · VS Code','Postman · Vite']),('Creative tools',['Figma · Blender · Canva','Ideas, prototypes & visual studies'])]
    b=''
    for i,(label,rows) in enumerate(groups):
        x=38 if mobile else 38+(i%3)*398;y=48+i*138 if mobile else 42+(i//3)*146
        b+=text(label,x,y,27 if mobile else 24,C['green'])+line(x,y+20,x+(524 if mobile else 346),y+20,'#c5c8b8')
        for n,row in enumerate(rows):b+=text(row,x,y+53+n*29,22 if mobile else 18,font='Manrope')
    svg('toolkit-mobile' if mobile else 'toolkit',600 if mobile else 1200,850 if mobile else 304,b,'The tools on my desk','A working toolkit, not an expertise ranking. Languages: TypeScript, JavaScript, Go, PHP, Python, Java, Dart. Frontend: React, Next.js, Tailwind CSS, Bootstrap. Backend: Node.js, Laravel, Spring Boot. Data and cloud: PostgreSQL, MySQL, Firebase, Vercel. Tools: Git, GitHub, VS Code, Postman, Vite. Creative tools: Figma, Blender, Canva.',C['ivory'])

def preview():
    b=raster('game-room',570,0,630,420)+text('A little world,',48,108,45,C['ivory'],tracking=-1.3)+text('made of pixels.',48,160,45,C['ivory'],tracking=-1.3)
    b+=text("Ryan's Little Coding Studio",48,213,23,'#b9cbb8')+text('Find 3 modules. Fix 2 bugs. Ship an idea.',48,259,19,'#e0e3d3',font='Manrope')+text('Keyboard · Touch · Text mode',48,297,17,'#b9cbb8',font='Manrope')
    b+=line(48,328,504,328,'#516459')+text('Game source included · Pages setup required',48,370,17,'#d2a875',font='Manrope')
    svg('game-preview',1200,420,b,"Ryan's Little Coding Studio — source preview",'Actual canvas frame from the included playable game. Collect three modules, fix two bugs, ship a garden journal. Keyboard, touch, and text mode. This link opens source; GitHub Pages has not been deployed.',C['ink'])
    b=text('A little world,',32,66,36,C['ivory'],tracking=-1)+text('made of pixels.',32,110,36,C['ivory'],tracking=-1)+text("Ryan's Little Coding Studio",32,156,22,'#b9cbb8')
    b+=raster('game-room',0,184,600,400)+text('Find 3 modules. Fix 2 bugs. Ship an idea.',32,621,23,'#e0e3d3',font='Manrope')+text('Keyboard · Touch · Text mode',32,658,21,'#b9cbb8',font='Manrope')+text('Game source included · Pages setup required',32,707,21,'#d2a875',font='Manrope')
    svg('game-preview-mobile',600,747,b,"Ryan's Little Coding Studio — source preview",'Actual game canvas. Three modules, two bugs, one small project. Keyboard, touch and text mode. Source only until GitHub Pages is enabled.',C['ink'])

activity()
if not args.activity_only:
    hero();hero(True)
    for row in PROJECTS:project(row);project(row,True)
    achievements();toolkit();toolkit(True)
    if (ROOT/'design/renders/game-room.png').exists():preview()
print('SVG assets written to',OUT)
