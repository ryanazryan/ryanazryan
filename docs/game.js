/* Original canvas art and a dependency-free game. All game effects stay in the browser. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const canvas = $('room'), ctx = canvas.getContext('2d');
  const motionPreference = matchMedia('(prefers-reduced-motion: reduce)');
  $('motion').checked = motionPreference.matches;
  motionPreference.addEventListener('change', e => { $('motion').checked = e.matches; });
  const tiles = 32, keys = new Set();
  const modules = [
    {id:'data', x:2,y:3, label:'Data module', note:'The data module gives every garden note a place to live.'},
    {id:'view', x:9,y:3, label:'Interface module', note:'The interface module makes the garden journal readable.'},
    {id:'logic',x:5,y:6,label:'Logic module',note:'The logic module joins the little pieces together.'}
  ];
  const bugs = [
    {id:'loop',x:3,y:5,label:'Off-by-one bug',title:'One step too far.',detail:'This loop reaches beyond the last item. Which condition keeps it inside the list?',code:'for (let i = 0; i <= notes.length; i++) {\n  render(notes[i]);\n}',choices:['i < notes.length','i > notes.length','i <= notes.length + 1'],answer:0,why:'Exactly. Array indexes stop one before the length.'},
    {id:'await',x:9,y:6,label:'Async bug',title:'A little patience.',detail:'loadNotes() returns a Promise. Inside an async function, how do we wait for the notes before rendering?',code:'async function openJournal() {\n  const notes = loadNotes();\n  render(notes);\n}',choices:['const notes = loadNotes;','const notes = await loadNotes();','const notes = null;'],answer:1,why:'Yes. await lets the notes arrive before rendering.'}
  ];
  const desk = {id:'desk',x:6,y:2,label:'Workstation'}, plant = {id:'plant',x:10,y:5,label:'The little plant'};
  let player, collected, fixed, started=false, won=false, activeBug=null, last=0, stepTime=0, lastMove=0;
  const blocked = new Set(['1,2','2,2','4,2','5,2','6,2','7,2','10,2','1,5','2,5','10,5']);
  const palette={ink:'#202624',dark:'#303f35',sage:'#8fa99b',green:'#405f54',ivory:'#f3efe6',amber:'#d2a875',wood:'#b68d62',shadow:'#765b43'};
  function say(text){$('status').textContent=text;}
  function clearKeys(){keys.clear();stepTime=0;}
  function reset(){
    clearKeys();player={x:6,y:6,drawX:6,drawY:6,facing:'down'};collected=new Set();fixed=new Set();won=false;started=false;activeBug=null;
    $('start-screen').hidden=false;$('win-screen').hidden=true;if($('puzzle').open)$('puzzle').close();
    $('phase').textContent='Ready when you are';say('The modules are ivory envelopes. Bugs are amber critters. Walk close, then interact.');sync();draw(0);
  }
  function start(){started=true;$('start-screen').hidden=true;$('phase').textContent='An idea in progress';say('Welcome in. Explore the room and gather the three ivory code modules.');sync();if(!$('text-mode').checked)canvas.focus();else document.querySelector('#destinations button')?.focus();}
  function available(){return [...modules.filter(m=>!collected.has(m.id)),...bugs.filter(b=>!fixed.has(b.id)),desk,plant];}
  function nearest(){return available().filter(o=>Math.abs(o.x-player.x)+Math.abs(o.y-player.y)<=1).sort((a,b)=>(Math.abs(a.x-player.x)+Math.abs(a.y-player.y))-(Math.abs(b.x-player.x)+Math.abs(b.y-player.y)))[0];}
  function sync(){
    const score=collected.size+fixed.size+(won?1:0);$('progress').value=score;$('progress').textContent=`${score} of 6`;$('progress-label').textContent=`${score} / 6`;
    $('module-count').textContent=`${collected.size} of 3 found`;$('bug-count').textContent=`${fixed.size} of 2 resolved`;
    $('check-modules').classList.toggle('done',collected.size===3);$('check-bugs').classList.toggle('done',fixed.size===2);$('check-ship').classList.toggle('done',won);
    const near=nearest();$('nearby').textContent=won?'A small project, ready for the world.':!started?'A warm desk, a few ideas, and room to explore.':near?`Nearby: ${near.label}. Press E or Interact.`:'Explore the studio. Look for ivory modules and amber bugs.';
    $('interact').disabled=$('touch-action').disabled=!started||won||!near;
    updateText();
  }
  function updateText(){
    const parent=$('destinations');
    if(!parent.children.length){[...modules,...bugs,desk,plant].forEach(o=>{const b=document.createElement('button');b.dataset.target=o.id;b.textContent=`Visit ${o.label.toLowerCase()}`;b.addEventListener('click',()=>act(o));parent.append(b);});}
    for(const b of parent.children){const done=collected.has(b.dataset.target)||fixed.has(b.dataset.target);b.disabled=!started||won||done;b.textContent=done?`${[...modules,...bugs].find(o=>o.id===b.dataset.target).label} — done`:`Visit ${[...modules,...bugs,desk,plant].find(o=>o.id===b.dataset.target).label.toLowerCase()}`;}
  }
  function act(o){
    if(!started||won||!o||$('puzzle').open)return;
    clearKeys();
    if(modules.some(m=>m.id===o.id)){if(collected.has(o.id))return;collected.add(o.id);say(o.note);}
    else if(bugs.some(b=>b.id===o.id)){if(fixed.has(o.id))return;openPuzzle(o);}
    else if(o.id==='plant')say('A small leaf, a small reminder: growth takes practice. You found the studio’s quiet corner.');
    else if(collected.size===3&&fixed.size===2){won=true;$('phase').textContent='A little idea, shipped';$('win-screen').hidden=false;say('Project complete. You collected all three modules, fixed both bugs, and shipped the garden journal.');$('again').focus();}
    else say(`The desk needs ${3-collected.size} more module${3-collected.size===1?'':'s'} and ${2-fixed.size} bug fix${2-fixed.size===1?'':'es'}. Take your time.`);
    sync();draw(0);
  }
  function openPuzzle(bug){
    activeBug=bug;$('puzzle-title').textContent=bug.title;$('puzzle-detail').textContent=bug.detail;$('puzzle-code').textContent=bug.code;$('answers').replaceChildren();$('feedback').textContent='Try a fix. You can always try again.';$('puzzle-done').hidden=true;
    bug.choices.forEach((choice,i)=>{const b=document.createElement('button');b.textContent=choice;b.addEventListener('click',()=>{
      if(fixed.has(bug.id))return;
      if(i===bug.answer){fixed.add(bug.id);$('feedback').textContent=bug.why;for(const a of $('answers').children)a.disabled=true;$('puzzle-done').hidden=false;$('puzzle-done').focus();say(`Fixed: ${bug.label}. ${bug.why}`);sync();}
      else {$('feedback').textContent='Not quite. Read the code once more and try another fix.';}
    });$('answers').append(b);});$('puzzle').showModal();
  }
  $('puzzle-done').addEventListener('click',()=>$('puzzle').close());
  $('puzzle').addEventListener('close',()=>{clearKeys();activeBug=null;if(!$('text-mode').checked)canvas.focus();else document.querySelector('#destinations button:not(:disabled)')?.focus();});
  function move(dir){
    if(!started||won||$('puzzle').open)return;
    const [dx,dy]={left:[-1,0],right:[1,0],up:[0,-1],down:[0,1]}[dir];
    const x=player.x+dx,y=player.y+dy;player.facing=dir;
    if(x>=1&&x<=10&&y>=2&&y<=6&&!blocked.has(`${x},${y}`)){player.x=x;player.y=y;lastMove=performance.now();}sync();
  }
  const map={ArrowUp:'up',w:'up',W:'up',ArrowDown:'down',s:'down',S:'down',ArrowLeft:'left',a:'left',A:'left',ArrowRight:'right',d:'right',D:'right'};
  canvas.addEventListener('keydown',e=>{if(map[e.key]){e.preventDefault();if(!keys.has(map[e.key])){move(map[e.key]);stepTime=performance.now()+160;}keys.add(map[e.key]);}else if(['e','E',' '].includes(e.key)){e.preventDefault();if(!e.repeat)act(nearest());}else if(e.key==='Escape'){clearKeys();canvas.blur();say('Movement paused. Focus the room or use a control to continue.');}});
  window.addEventListener('keyup',e=>{if(map[e.key])keys.delete(map[e.key]);});window.addEventListener('blur',clearKeys);canvas.addEventListener('blur',clearKeys);document.addEventListener('visibilitychange',clearKeys);
  for(const b of document.querySelectorAll('[data-dir]')){
    b.addEventListener('pointerdown',e=>{e.preventDefault();b.setPointerCapture(e.pointerId);clearKeys();move(b.dataset.dir);keys.add(b.dataset.dir);stepTime=performance.now()+160;});
    for(const type of ['pointerup','pointercancel','lostpointercapture'])b.addEventListener(type,clearKeys);
    b.addEventListener('click',e=>{if(e.detail===0)move(b.dataset.dir);});
  }
  $('interact').addEventListener('click',()=>act(nearest()));$('touch-action').addEventListener('click',()=>act(nearest()));
  $('start').addEventListener('click',start);$('restart').addEventListener('click',()=>{reset();$('start').focus();});$('again').addEventListener('click',()=>{reset();start();});
  $('text-mode').addEventListener('change',()=>{clearKeys();$('text-actions').hidden=!$('text-mode').checked;canvas.tabIndex=$('text-mode').checked?-1:0;if($('text-mode').checked)say('Text mode enabled. Start the project, then choose places under “The studio, in words.”');});
  const R=(x,y,w,h,c)=>{ctx.fillStyle=c;ctx.fillRect(Math.round(x),Math.round(y),w,h);};
  function line(x,y,w,c){R(x,y,w,1,c);}
  function plantSprite(x,y){R(x+4,y+17,14,12,'#9b6a48');R(x+2,y+15,18,4,'#d0a879');R(x+9,y,3,18,'#567a58');R(x,y+5,10,6,'#698d65');R(x+11,y+1,11,7,'#739871');R(x+3,y+9,8,5,'#8fa777');R(x+12,y+10,12,5,'#476b53');R(x+4,y+5,4,2,'#afc19a');}
  function book(x,y,h,c){R(x,y,5,h,c);R(x+1,y+2,3,1,'#d8c8a4');R(x+1,y+h-4,3,1,'#d8c8a4');}
  function moduleSprite(x,y){R(x+1,y+3,18,14,'#594f3d');R(x,y,18,14,'#ede6cb');R(x+2,y+2,14,10,'#fffae8');R(x+4,y+5,2,4,'#405f54');R(x+6,y+3,2,2,'#405f54');R(x+6,y+9,2,2,'#405f54');R(x+12,y+5,2,4,'#405f54');R(x+10,y+3,2,2,'#405f54');R(x+10,y+9,2,2,'#405f54');}
  function bugSprite(x,y,t){R(x+4,y+3,12,12,'#523e2f');R(x+4,y,12,12,'#d2a875');R(x+7,y-3,6,4,'#d2a875');R(x+6,y+3,2,2,'#202624');R(x+12,y+3,2,2,'#202624');R(x+9,y+7,2,6,'#9b6c43');for(let i=0;i<3;i++){R(x+(t?0:1),y+i*4+2,4,2,'#ba8c59');R(x+16,y+i*4+2,4,2,'#ba8c59');}}
  function person(x,y,t){
    R(x-7,y+9,18,4,'#7e644b');R(x-5,y-10,13,13,'#232d27');R(x-3,y-14,10,5,'#232d27');R(x-3,y-9,10,9,'#ddb588');R(x-5,y-9,3,4,'#232d27');R(x+5,y-10,3,5,'#232d27');
    if(player.facing!=='up'){R(x-1,y-6,2,2,'#202624');R(x+4,y-6,2,2,'#202624');R(x+2,y-2,3,1,'#a57654');}else R(x-3,y-10,10,6,'#232d27');
    R(x-5,y,13,9,'#405f54');R(x-7,y+1,3,7,'#8fa99b');R(x+8,y+1,3,7,'#8fa99b');R(x-7,y+7,3,3,'#ddb588');R(x+8,y+7,3,3,'#ddb588');R(x,y+1,2,6,'#a1b29b');R(x-4,y+9,5,5+(t?1:0),'#29382f');R(x+3,y+9,5,5+(t?0:1),'#29382f');R(x-5,y+13,6,2,'#ece2c6');R(x+3,y+13,6,2,'#ece2c6');
  }
  function draw(time){
    if(!ctx)return;
    const still=$('motion').checked,t=still?0:time;ctx.imageSmoothingEnabled=false;
    R(0,0,384,256,'#202624');R(16,18,352,220,'#655140');R(16,18,352,74,'#8d9b7c');R(20,22,344,66,'#a9b398');
    for(let i=0;i<12;i++)R(20+i*30,22,1,66,'#9eaa8e');
    R(20,88,344,146,'#b68d62');for(let y=92;y<234;y+=16){line(20,y,344,'#98744e');for(let x=20+(y%32?25:0);x<364;x+=48){R(x,y,1,16,'#a17a51');line(x+5,y+9,24,'#c49a6c');}}
    R(16,88,352,5,'#66513e');R(16,234,352,8,'#594b39');R(20,234,344,2,'#ddbc89');R(16,22,4,216,'#66513e');R(364,22,4,216,'#66513e');
    // Window, sunset, distant hills and curtains.
    R(126,26,102,55,'#596c5c');R(130,30,94,47,'#c7cdb2');R(132,32,90,22,'#e4c48f');R(132,54,90,21,'#a4b398');R(194,37,12,12,'#f1deb2');R(132,66,90,9,'#728e77');R(146,60,17,15,'#91a087');R(166,64,25,11,'#728a72');R(180,30,3,47,'#f3e5be');R(130,54,94,3,'#f3e5be');R(123,77,109,4,'#e2cba3');R(120,26,7,51,'#c4c3a5');R(225,26,7,51,'#c4c3a5');
    // Back-left bookshelf.
    R(36,44,65,46,'#654e39');R(39,46,59,42,'#826347');for(const yy of [46,66]){book(44,yy+2,15,'#405f54');book(50,yy+4,13,'#b99b6d');book(57,yy+1,16,'#8c9b80');book(64,yy+3,14,'#61747a');book(72,yy+4,13,'#d4bc8d');R(81,yy+10,10,6,'#b68d62');R(40,yy+18,57,3,'#c39d70');}
    // Workstation with wood top, monitor, code and a warm lamp.
    R(126,109,135,8,'#846649');R(132,111,7,27,'#6d543f');R(246,111,7,27,'#6d543f');R(126,90,135,22,'#dab27c');R(126,109,135,3,'#a47c51');R(133,95,119,1,'#e7c698');R(164,65,62,38,'#36473c');R(167,68,56,29,'#202f29');R(189,101,11,5,'#526051');R(183,106,24,3,'#526051');
    for(let i=0;i<6;i++){R(172,72+i*4,2,1,'#607768');R(178+(i%2)*3,72+i*4,16+(i%3)*5,1,i%3===0?'#d2a875':'#8fa99b');}R(211,89,1,4,Math.sin(t/700)>0?'#bac6a6':'#202f29');R(177,111,35,6,'#f0dfb9');for(let i=0;i<8;i++)R(180+i*4,113,2,1,'#899283');R(222,111,5,5,'#455747');R(142,83,2,16,'#8b6e45');R(136,97,15,3,'#c19d61');R(135,79,17,5,'#d2a875');R(137,76,13,3,'#dfbb76');R(139,84,9,2,'#ffdeb0');
    ctx.fillStyle=`rgba(255,215,147,${still?.08:.08+Math.sin(t/1600)*.018})`;ctx.fillRect(130,87,30,18);
    // Server, notes, plant and sofa.
    R(316,59,33,49,'#455449');R(319,62,27,43,'#29382e');for(let i=0;i<3;i++){R(322,67+i*12,22,9,'#394a3c');R(324,70+i*12,11,2,'#708675');R(339,70+i*12,2,2,'#d2a875');}R(273,38,24,25,'#ecdfbe');R(276,42,16,1,'#8fa99b');R(276,47,12,1,'#9ca58e');R(281,52,5,5,'#8fa99b');R(284,35,3,5,'#b59361');plantSprite(334,140);
    R(36,159,62,32,'#586e54');R(38,150,58,27,'#6f8968');R(39,160,55,13,'#809676');R(36,157,7,24,'#8fa07f');R(91,157,7,24,'#8fa07f');R(45,174,44,4,'#536b50');R(43,183,5,11,'#6d543f');R(87,183,5,11,'#6d543f');R(47,153,14,14,'#bdba91');
    // Rug and a little wooden stool.
    R(126,146,133,73,'#8e7858');R(130,148,125,67,'#c7b78d');R(134,152,117,59,'#91a087');R(139,157,107,49,'#86977b');for(let i=0;i<14;i++){R(132+i*9,145,2,4,'#d6c59a');R(132+i*9,215,2,5,'#d6c59a');}for(let i=0;i<7;i++)line(140,160+i*7,104,'#93a284');R(275,155,22,14,'#775c40');R(273,151,26,8,'#d2ad77');R(277,169,3,7,'#775c40');R(291,169,3,7,'#775c40');R(281,147,9,4,'#ede1be');R(284,140,1,4,'#c9c7a4');
    modules.forEach(m=>{if(!collected.has(m.id)){const bob=still?0:Math.round(Math.sin(t/600+m.x)*1);moduleSprite(m.x*32+7,m.y*32+7+bob);}});
    bugs.forEach(b=>{if(!fixed.has(b.id))bugSprite(b.x*32+6,b.y*32+7,Math.floor(t/600)%2);});
    if(collected.size===3&&fixed.size===2&&!won){R(237,74,11,11,'#ede4c8');R(241,77,3,5,'#405f54');R(239,80,2,2,'#405f54');}
    if(!still){player.drawX+=(player.x-player.drawX)*.35;player.drawY+=(player.y-player.drawY)*.35;}else{player.drawX=player.x;player.drawY=player.y;}
    person(Math.round(player.drawX*tiles+16),Math.round(player.drawY*tiles+12),!still&&performance.now()-lastMove<180&&Math.floor(t/90)%2);
    // A composed border and brass floor studs.
    for(let x=28;x<363;x+=32)R(x,238,2,1,'#a78961');
  }
  function frame(time){const dt=Math.min(time-last,100);last=time;if(keys.size&&time>=stepTime){move([...keys].at(-1));stepTime=time+145;}draw(time);requestAnimationFrame(frame);}
  reset();requestAnimationFrame(frame);
})();
