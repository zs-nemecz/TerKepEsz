/*************************** 
 * Terkepesz-Encoding Test *
 ***************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.804, 0.804, 0.961]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'terkepesz-encoding';  // from the Builder filename that created this script
let expInfo = {'ID': '', 'practice': '1'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(start_encodingRoutineBegin());
flowScheduler.add(start_encodingRoutineEachFrame());
flowScheduler.add(start_encodingRoutineEnd());
flowScheduler.add(enc_instructions_1RoutineBegin());
flowScheduler.add(enc_instructions_1RoutineEachFrame());
flowScheduler.add(enc_instructions_1RoutineEnd());
flowScheduler.add(enc_instructions_2RoutineBegin());
flowScheduler.add(enc_instructions_2RoutineEachFrame());
flowScheduler.add(enc_instructions_2RoutineEnd());
flowScheduler.add(enc_instructions_3RoutineBegin());
flowScheduler.add(enc_instructions_3RoutineEachFrame());
flowScheduler.add(enc_instructions_3RoutineEnd());
flowScheduler.add(start_practiceRoutineBegin());
flowScheduler.add(start_practiceRoutineEachFrame());
flowScheduler.add(start_practiceRoutineEnd());
const enc_practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(enc_practice_trialsLoopBegin, enc_practice_trialsLoopScheduler);
flowScheduler.add(enc_practice_trialsLoopScheduler);
flowScheduler.add(enc_practice_trialsLoopEnd);
flowScheduler.add(end_practiceRoutineBegin());
flowScheduler.add(end_practiceRoutineEachFrame());
flowScheduler.add(end_practiceRoutineEnd());
const enc_runsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(enc_runsLoopBegin, enc_runsLoopScheduler);
flowScheduler.add(enc_runsLoopScheduler);
flowScheduler.add(enc_runsLoopEnd);
flowScheduler.add(inter_task_breakRoutineBegin());
flowScheduler.add(inter_task_breakRoutineEachFrame());
flowScheduler.add(inter_task_breakRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://docs.google.com/forms/d/e/1FAIpQLSe-JyQOJB2rcwl0jYrK_pOr_J8RNK4YRzq_I4WmRa4Pfox_aA/viewform?usp=sf_link', '');

  return Scheduler.Event.NEXT;
}


var start_encodingClock;
var start_encoding_text;
var tables;
var trial_table;
var stimuli_table;
var enc_instructions_1Clock;
var enc_instructions_1_text;
var enc_instructions_1_image;
var enc_instructions_1_key;
var instructions_1_continue;
var enc_instructions_2Clock;
var enc_instructions_2_text;
var enc_instructions_2_image;
var enc_instructions_2_key;
var instructions_2_continue;
var enc_instructions_3Clock;
var enc_instructions_3_text;
var enc_instructions_3_key;
var enc_instructions_3_continue;
var start_practiceClock;
var start_practice_text;
var practice;
var enc_practice_fxClock;
var enc_practice_fx_interior;
var enc_practice_fx_cross;
var enc_practice_fx_key;
var enc_practice_trialClock;
var w_size;
var x_size;
var y_size;
var scr_resolution;
var enc_practice_trial_interior;
var enc_practice_trial_main_image;
var enc_practice_trial_key;
var enc_practice_feedbackClock;
var enc_practice_feedback_interior;
var enc_practice_feedback_image;
var enc_practice_feedback_text;
var end_practiceClock;
var end_practice_text;
var end_practice_key;
var end_practice_continue;
var start_MRClock;
var start_MR_text;
var start_MR_trigger;
var trigger_key;
var trigger_time;
var start_enc_runClock;
var start_enc_run_text;
var enc_fxClock;
var enc_fx_interior;
var enc_fx_cross;
var enc_fx_key;
var enc_trialClock;
var enc_trial_interior;
var enc_trial_main_image;
var enc_trial_key;
var end_enc_runClock;
var end_enc_run_text;
var enc_run_end_key;
var enc_run_end_continue;
var inter_task_breakClock;
var inter_task_break_text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "start_encoding"
  start_encodingClock = new util.Clock();
  start_encoding_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_encoding_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  tables = ["0","1","2"];
  trial_table = tables[Math.floor(Math.random() * tables.length)];
  stimuli_table = (("stimuli_tables/encoding_trials_" + trial_table) + ".csv");
  
  // Initialize components for Routine "enc_instructions_1"
  enc_instructions_1Clock = new util.Clock();
  enc_instructions_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_1_text',
    text: 'Ön ennek a modern képgalériának a kurátora. \n\nA legújabb kiállításra a vártnál több kép érkezett.\nKurátorként az Ön feladata lesz eldönteni, mely képeket válogatjuk be a kiállított darabok közé, és hogy a kép illeszkedik-e a galéria adott pontjára.\n\nAz Ön ideje nagyon drága a galériának, így a döntésre egy-egy képről csak 3 másodperce lesz.',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], height: 0.03,  wrapWidth: 0.65, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  enc_instructions_1_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_instructions_1_image', units : 'norm', 
    image : 'stimuli/GalleryBuildingFromOutside.jpg', mask : undefined,
    ori : 0, pos : [0.4688, 0.0], size : [0.625, 0.8333],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_instructions_1_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instructions_1_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_1_continue',
    text: 'A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "enc_instructions_2"
  enc_instructions_2Clock = new util.Clock();
  enc_instructions_2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_2_text',
    text: 'Ez a kiállítóterem, nézze meg figyelmesen. \n\nA feladat során a képek a falra vetítve jelennek meg, azon a helyen, ahol kiállításra kerülhetnek. A képek előtt egy keresztet fog látni, ami jelzi a képek pontos helyét.\n\nDöntse el a képekről, hogy ki legyenek-e állítva a bemutatott helyen. A beválogatott képek száma nincsen korlátozva. Minden egyes képről Ön dönt. Ha több képet válogat be, mint amennyi a galériában elfér, akkor a képeket az év során felváltva állítjuk ki.\n\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ. ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), 0], height: 0.03,  wrapWidth: 0.5, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  enc_instructions_2_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_instructions_2_image', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0.4427, 0], size : [0.7604, 0.8185],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_instructions_2_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instructions_2_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_2_continue',
    text: 'A folytatáshoz nyomja le a gombot a jobb hüvelyujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "enc_instructions_3"
  enc_instructions_3Clock = new util.Clock();
  enc_instructions_3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_3_text',
    text: 'Az első feladat nagyjából 25 percet vesz igénybe, közben két rövid szünettel.\n\nA jobb mutatóujjával jelölje azokat a képeket, amelyek maradhatnak a galériában, a bemutatott helyen.\n\nA bal mutatóujjával jelölje a képeket, amelyek nem maradnak kiállítva a bemutatott helyen. \n\nMost a gyakorló feladat következik. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  enc_instructions_3_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  enc_instructions_3_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_3_continue',
    text: 'Ha készen áll a gyakorlásra, nyomja meg a gombot a jobb hüvelykujjával.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "start_practice"
  start_practiceClock = new util.Clock();
  start_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_practice_text',
    text: 'Kezdődik a gyakorlás...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  practice = Number.parseInt(expInfo["practice"]);
  
  // Initialize components for Routine "enc_practice_fx"
  enc_practice_fxClock = new util.Clock();
  enc_practice_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_practice_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  enc_practice_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_practice_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  enc_practice_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "enc_practice_trial"
  enc_practice_trialClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  enc_practice_trial_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_practice_trial_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_practice_trial_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_practice_trial_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  enc_practice_trial_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "enc_practice_feedback"
  enc_practice_feedbackClock = new util.Clock();
  enc_practice_feedback_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_practice_feedback_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_practice_feedback_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_practice_feedback_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  enc_practice_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_practice_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "end_practice"
  end_practiceClock = new util.Clock();
  end_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_practice_text',
    text: 'Ez volt a gyakorlás. A feladat következik. \nA feladat során már nem kap visszajelzést a döntéséről. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 0.8, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  end_practice_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  end_practice_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_practice_continue',
    text: 'A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "start_MR"
  start_MRClock = new util.Clock();
  start_MR_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_MR_text',
    text: 'A vizsgálatvezető indítja a szkennert...',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  start_MR_trigger = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  trigger_key = "s";
  function get_current_trigger_time() {
      var trigger;
      trigger = (globalClock.getTime() - trigger_time);
      thisExp.addData("triggers", trigger);
      thisExp.nextEntry();
      return trigger;
  }
  trigger_time = 0;
  psychoJS.event.globalKeys.add({"key": trigger_key, "func": get_current_trigger_time});
  
  // Initialize components for Routine "start_enc_run"
  start_enc_runClock = new util.Clock();
  start_enc_run_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_enc_run_text',
    text: 'Kezdődik a feladat...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "enc_fx"
  enc_fxClock = new util.Clock();
  enc_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  enc_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  enc_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "enc_trial"
  enc_trialClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  enc_trial_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_trial_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_trial_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_trial_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  enc_trial_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_enc_run"
  end_enc_runClock = new util.Clock();
  end_enc_run_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_enc_run_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  enc_run_end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  enc_run_end_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_run_end_continue',
    text: 'A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "inter_task_break"
  inter_task_breakClock = new util.Clock();
  inter_task_break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'inter_task_break_text',
    text: 'Most kivesszük Önt a szkennerből.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var start;
var end;
var step;
var n_runs;
var run_counter;
var start_encodingComponents;
function start_encodingRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_encoding'-------
    t = 0;
    start_encodingClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    start_encoding_text.setText('Első feladat\nGaléria berendezés');
    start = 0;
    end = 0;
    step = 1;
    n_runs = 3;
    run_counter = 0;
    
    // keep track of which components have finished
    start_encodingComponents = [];
    start_encodingComponents.push(start_encoding_text);
    
    for (const thisComponent of start_encodingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
var continueRoutine;
function start_encodingRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'start_encoding'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = start_encodingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_encoding_text* updates
    if (t >= 0.0 && start_encoding_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_encoding_text.tStart = t;  // (not accounting for frame time here)
      start_encoding_text.frameNStart = frameN;  // exact frame index
      
      start_encoding_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_encoding_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_encoding_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_encodingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_encodingRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'start_encoding'-------
    for (const thisComponent of start_encodingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _enc_instructions_1_key_allKeys;
var enc_instructions_1Components;
function enc_instructions_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_instructions_1'-------
    t = 0;
    enc_instructions_1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    enc_instructions_1_key.keys = undefined;
    enc_instructions_1_key.rt = undefined;
    _enc_instructions_1_key_allKeys = [];
    // keep track of which components have finished
    enc_instructions_1Components = [];
    enc_instructions_1Components.push(enc_instructions_1_text);
    enc_instructions_1Components.push(enc_instructions_1_image);
    enc_instructions_1Components.push(enc_instructions_1_key);
    enc_instructions_1Components.push(instructions_1_continue);
    
    for (const thisComponent of enc_instructions_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_instructions_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_instructions_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_instructions_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_instructions_1_text* updates
    if (t >= 0.0 && enc_instructions_1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_1_text.tStart = t;  // (not accounting for frame time here)
      enc_instructions_1_text.frameNStart = frameN;  // exact frame index
      
      enc_instructions_1_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_1_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_1_text.setAutoDraw(false);
    }
    
    // *enc_instructions_1_image* updates
    if (t >= 0.0 && enc_instructions_1_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_1_image.tStart = t;  // (not accounting for frame time here)
      enc_instructions_1_image.frameNStart = frameN;  // exact frame index
      
      enc_instructions_1_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_1_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_1_image.setAutoDraw(false);
    }
    
    // *enc_instructions_1_key* updates
    if (t >= 5.0 && enc_instructions_1_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_1_key.tStart = t;  // (not accounting for frame time here)
      enc_instructions_1_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_instructions_1_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_1_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_1_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_1_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_1_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_instructions_1_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_instructions_1_key.getKeys({keyList: ['d'], waitRelease: false});
      _enc_instructions_1_key_allKeys = _enc_instructions_1_key_allKeys.concat(theseKeys);
      if (_enc_instructions_1_key_allKeys.length > 0) {
        enc_instructions_1_key.keys = _enc_instructions_1_key_allKeys[_enc_instructions_1_key_allKeys.length - 1].name;  // just the last key pressed
        enc_instructions_1_key.rt = _enc_instructions_1_key_allKeys[_enc_instructions_1_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instructions_1_continue* updates
    if (t >= 5.0 && instructions_1_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_1_continue.tStart = t;  // (not accounting for frame time here)
      instructions_1_continue.frameNStart = frameN;  // exact frame index
      
      instructions_1_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (instructions_1_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      instructions_1_continue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_instructions_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_instructions_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_instructions_1'-------
    for (const thisComponent of enc_instructions_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_instructions_1_key.keys', enc_instructions_1_key.keys);
    if (typeof enc_instructions_1_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_1_key.rt', enc_instructions_1_key.rt);
        routineTimer.reset();
        }
    
    enc_instructions_1_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enc_instructions_2_key_allKeys;
var enc_instructions_2Components;
function enc_instructions_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_instructions_2'-------
    t = 0;
    enc_instructions_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    enc_instructions_2_key.keys = undefined;
    enc_instructions_2_key.rt = undefined;
    _enc_instructions_2_key_allKeys = [];
    // keep track of which components have finished
    enc_instructions_2Components = [];
    enc_instructions_2Components.push(enc_instructions_2_text);
    enc_instructions_2Components.push(enc_instructions_2_image);
    enc_instructions_2Components.push(enc_instructions_2_key);
    enc_instructions_2Components.push(instructions_2_continue);
    
    for (const thisComponent of enc_instructions_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_instructions_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_instructions_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_instructions_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_instructions_2_text* updates
    if (t >= 0.0 && enc_instructions_2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_text.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_text.frameNStart = frameN;  // exact frame index
      
      enc_instructions_2_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_text.setAutoDraw(false);
    }
    
    // *enc_instructions_2_image* updates
    if (t >= 0.0 && enc_instructions_2_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_image.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_image.frameNStart = frameN;  // exact frame index
      
      enc_instructions_2_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_image.setAutoDraw(false);
    }
    
    // *enc_instructions_2_key* updates
    if (t >= 5.0 && enc_instructions_2_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_key.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_instructions_2_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_instructions_2_key.getKeys({keyList: ['d'], waitRelease: false});
      _enc_instructions_2_key_allKeys = _enc_instructions_2_key_allKeys.concat(theseKeys);
      if (_enc_instructions_2_key_allKeys.length > 0) {
        enc_instructions_2_key.keys = _enc_instructions_2_key_allKeys[_enc_instructions_2_key_allKeys.length - 1].name;  // just the last key pressed
        enc_instructions_2_key.rt = _enc_instructions_2_key_allKeys[_enc_instructions_2_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instructions_2_continue* updates
    if (t >= 5.0 && instructions_2_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_2_continue.tStart = t;  // (not accounting for frame time here)
      instructions_2_continue.frameNStart = frameN;  // exact frame index
      
      instructions_2_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (instructions_2_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      instructions_2_continue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_instructions_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_instructions_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_instructions_2'-------
    for (const thisComponent of enc_instructions_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_instructions_2_key.keys', enc_instructions_2_key.keys);
    if (typeof enc_instructions_2_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_2_key.rt', enc_instructions_2_key.rt);
        routineTimer.reset();
        }
    
    enc_instructions_2_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enc_instructions_3_key_allKeys;
var enc_instructions_3Components;
function enc_instructions_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_instructions_3'-------
    t = 0;
    enc_instructions_3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    enc_instructions_3_key.keys = undefined;
    enc_instructions_3_key.rt = undefined;
    _enc_instructions_3_key_allKeys = [];
    // keep track of which components have finished
    enc_instructions_3Components = [];
    enc_instructions_3Components.push(enc_instructions_3_text);
    enc_instructions_3Components.push(enc_instructions_3_key);
    enc_instructions_3Components.push(enc_instructions_3_continue);
    
    for (const thisComponent of enc_instructions_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_instructions_3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_instructions_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_instructions_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_instructions_3_text* updates
    if (t >= 0.0 && enc_instructions_3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_3_text.tStart = t;  // (not accounting for frame time here)
      enc_instructions_3_text.frameNStart = frameN;  // exact frame index
      
      enc_instructions_3_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_3_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_3_text.setAutoDraw(false);
    }
    
    // *enc_instructions_3_key* updates
    if (t >= 5.0 && enc_instructions_3_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_3_key.tStart = t;  // (not accounting for frame time here)
      enc_instructions_3_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_instructions_3_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_3_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_3_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_3_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_3_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_instructions_3_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_instructions_3_key.getKeys({keyList: ['d'], waitRelease: false});
      _enc_instructions_3_key_allKeys = _enc_instructions_3_key_allKeys.concat(theseKeys);
      if (_enc_instructions_3_key_allKeys.length > 0) {
        enc_instructions_3_key.keys = _enc_instructions_3_key_allKeys[_enc_instructions_3_key_allKeys.length - 1].name;  // just the last key pressed
        enc_instructions_3_key.rt = _enc_instructions_3_key_allKeys[_enc_instructions_3_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *enc_instructions_3_continue* updates
    if (t >= 5.0 && enc_instructions_3_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_3_continue.tStart = t;  // (not accounting for frame time here)
      enc_instructions_3_continue.frameNStart = frameN;  // exact frame index
      
      enc_instructions_3_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_3_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_3_continue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_instructions_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_instructions_3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_instructions_3'-------
    for (const thisComponent of enc_instructions_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_instructions_3_key.keys', enc_instructions_3_key.keys);
    if (typeof enc_instructions_3_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_3_key.rt', enc_instructions_3_key.rt);
        routineTimer.reset();
        }
    
    enc_instructions_3_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var start_practiceComponents;
function start_practiceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_practice'-------
    t = 0;
    start_practiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    start_practiceComponents = [];
    start_practiceComponents.push(start_practice_text);
    
    for (const thisComponent of start_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function start_practiceRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'start_practice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = start_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_practice_text* updates
    if (t >= 0.0 && start_practice_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_practice_text.tStart = t;  // (not accounting for frame time here)
      start_practice_text.frameNStart = frameN;  // exact frame index
      
      start_practice_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_practice_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_practice_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_practiceRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'start_practice'-------
    for (const thisComponent of start_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var enc_practice_trials;
var currentLoop;
function enc_practice_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_practice_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: $practice, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli_tables/encoding_practice_trials.csv',
    seed: undefined, name: 'enc_practice_trials'
  });
  psychoJS.experiment.addLoop(enc_practice_trials); // add the loop to the experiment
  currentLoop = enc_practice_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisEnc_practice_trial of enc_practice_trials) {
    const snapshot = enc_practice_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(enc_practice_fxRoutineBegin(snapshot));
    thisScheduler.add(enc_practice_fxRoutineEachFrame(snapshot));
    thisScheduler.add(enc_practice_fxRoutineEnd(snapshot));
    thisScheduler.add(enc_practice_trialRoutineBegin(snapshot));
    thisScheduler.add(enc_practice_trialRoutineEachFrame(snapshot));
    thisScheduler.add(enc_practice_trialRoutineEnd(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineBegin(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function enc_practice_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(enc_practice_trials);

  return Scheduler.Event.NEXT;
}


var enc_runs;
function enc_runsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_runs = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'enc_runs'
  });
  psychoJS.experiment.addLoop(enc_runs); // add the loop to the experiment
  currentLoop = enc_runs;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisEnc_run of enc_runs) {
    const snapshot = enc_runs.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(start_MRRoutineBegin(snapshot));
    thisScheduler.add(start_MRRoutineEachFrame(snapshot));
    thisScheduler.add(start_MRRoutineEnd(snapshot));
    thisScheduler.add(start_enc_runRoutineBegin(snapshot));
    thisScheduler.add(start_enc_runRoutineEachFrame(snapshot));
    thisScheduler.add(start_enc_runRoutineEnd(snapshot));
    const enc_trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(enc_trialsLoopBegin, enc_trialsLoopScheduler);
    thisScheduler.add(enc_trialsLoopScheduler);
    thisScheduler.add(enc_trialsLoopEnd);
    thisScheduler.add(end_enc_runRoutineBegin(snapshot));
    thisScheduler.add(end_enc_runRoutineEachFrame(snapshot));
    thisScheduler.add(end_enc_runRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var enc_trials;
function enc_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, stimuli_table, selection),
    seed: undefined, name: 'enc_trials'
  });
  psychoJS.experiment.addLoop(enc_trials); // add the loop to the experiment
  currentLoop = enc_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisEnc_trial of enc_trials) {
    const snapshot = enc_trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(enc_fxRoutineBegin(snapshot));
    thisScheduler.add(enc_fxRoutineEachFrame(snapshot));
    thisScheduler.add(enc_fxRoutineEnd(snapshot));
    thisScheduler.add(enc_trialRoutineBegin(snapshot));
    thisScheduler.add(enc_trialRoutineEachFrame(snapshot));
    thisScheduler.add(enc_trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function enc_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(enc_trials);

  return Scheduler.Event.NEXT;
}


function enc_runsLoopEnd() {
  psychoJS.experiment.removeLoop(enc_runs);

  return Scheduler.Event.NEXT;
}


var _enc_practice_fx_key_allKeys;
var enc_practice_fxComponents;
function enc_practice_fxRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_practice_fx'-------
    t = 0;
    enc_practice_fxClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    enc_practice_fx_cross.setPos([CurrentX, CurrentY]);
    enc_practice_fx_key.keys = undefined;
    enc_practice_fx_key.rt = undefined;
    _enc_practice_fx_key_allKeys = [];
    // keep track of which components have finished
    enc_practice_fxComponents = [];
    enc_practice_fxComponents.push(enc_practice_fx_interior);
    enc_practice_fxComponents.push(enc_practice_fx_cross);
    enc_practice_fxComponents.push(enc_practice_fx_key);
    
    for (const thisComponent of enc_practice_fxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_practice_fxRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_practice_fx'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_practice_fxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_practice_fx_interior* updates
    if (t >= 0.0 && enc_practice_fx_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_fx_interior.tStart = t;  // (not accounting for frame time here)
      enc_practice_fx_interior.frameNStart = frameN;  // exact frame index
      
      enc_practice_fx_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_fx_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_fx_interior.setAutoDraw(false);
    }
    
    // *enc_practice_fx_cross* updates
    if (t >= 0.0 && enc_practice_fx_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_fx_cross.tStart = t;  // (not accounting for frame time here)
      enc_practice_fx_cross.frameNStart = frameN;  // exact frame index
      
      enc_practice_fx_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_fx_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_fx_cross.setAutoDraw(false);
    }
    
    // *enc_practice_fx_key* updates
    if (t >= 0.0 && enc_practice_fx_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_fx_key.tStart = t;  // (not accounting for frame time here)
      enc_practice_fx_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_practice_fx_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_practice_fx_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_practice_fx_key.clearEvents(); });
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_fx_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_fx_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_practice_fx_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_practice_fx_key.getKeys({keyList: ['b', 'c'], waitRelease: false});
      _enc_practice_fx_key_allKeys = _enc_practice_fx_key_allKeys.concat(theseKeys);
      if (_enc_practice_fx_key_allKeys.length > 0) {
        enc_practice_fx_key.keys = _enc_practice_fx_key_allKeys[_enc_practice_fx_key_allKeys.length - 1].name;  // just the last key pressed
        enc_practice_fx_key.rt = _enc_practice_fx_key_allKeys[_enc_practice_fx_key_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_practice_fxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_practice_fxRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_practice_fx'-------
    for (const thisComponent of enc_practice_fxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_practice_fx_key.keys', enc_practice_fx_key.keys);
    if (typeof enc_practice_fx_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_practice_fx_key.rt', enc_practice_fx_key.rt);
        }
    
    enc_practice_fx_key.stop();
    // the Routine "enc_practice_fx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _enc_practice_trial_key_allKeys;
var enc_practice_trialComponents;
function enc_practice_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_practice_trial'-------
    t = 0;
    enc_practice_trialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    w_size = psychoJS.window.size;
    
    x_size = w_size[0];
    y_size = w_size[1];
    
    scr_resolution = (x_size / y_size);
    
    enc_practice_trial_main_image.setPos([CurrentX, CurrentY]);
    enc_practice_trial_main_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    enc_practice_trial_main_image.setImage(CurrentImage);
    enc_practice_trial_key.keys = undefined;
    enc_practice_trial_key.rt = undefined;
    _enc_practice_trial_key_allKeys = [];
    // keep track of which components have finished
    enc_practice_trialComponents = [];
    enc_practice_trialComponents.push(enc_practice_trial_interior);
    enc_practice_trialComponents.push(enc_practice_trial_main_image);
    enc_practice_trialComponents.push(enc_practice_trial_key);
    
    for (const thisComponent of enc_practice_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_practice_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_practice_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_practice_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_practice_trial_interior* updates
    if (t >= 0.0 && enc_practice_trial_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_trial_interior.tStart = t;  // (not accounting for frame time here)
      enc_practice_trial_interior.frameNStart = frameN;  // exact frame index
      
      enc_practice_trial_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_trial_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_trial_interior.setAutoDraw(false);
    }
    
    // *enc_practice_trial_main_image* updates
    if (t >= 0.0 && enc_practice_trial_main_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_trial_main_image.tStart = t;  // (not accounting for frame time here)
      enc_practice_trial_main_image.frameNStart = frameN;  // exact frame index
      
      enc_practice_trial_main_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_trial_main_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_trial_main_image.setAutoDraw(false);
    }
    
    // *enc_practice_trial_key* updates
    if (t >= 0.0 && enc_practice_trial_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_trial_key.tStart = t;  // (not accounting for frame time here)
      enc_practice_trial_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_practice_trial_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_practice_trial_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_practice_trial_key.clearEvents(); });
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_trial_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_trial_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_practice_trial_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_practice_trial_key.getKeys({keyList: ['b', 'c'], waitRelease: false});
      _enc_practice_trial_key_allKeys = _enc_practice_trial_key_allKeys.concat(theseKeys);
      if (_enc_practice_trial_key_allKeys.length > 0) {
        enc_practice_trial_key.keys = _enc_practice_trial_key_allKeys[_enc_practice_trial_key_allKeys.length - 1].name;  // just the last key pressed
        enc_practice_trial_key.rt = _enc_practice_trial_key_allKeys[_enc_practice_trial_key_allKeys.length - 1].rt;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_practice_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_practice_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_practice_trial'-------
    for (const thisComponent of enc_practice_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_practice_trial_key.keys', enc_practice_trial_key.keys);
    if (typeof enc_practice_trial_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_practice_trial_key.rt', enc_practice_trial_key.rt);
        }
    
    enc_practice_trial_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var response;
var feedback_text;
var enc_practice_feedbackComponents;
function enc_practice_feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_practice_feedback'-------
    t = 0;
    enc_practice_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    response = enc_practice_trial_key.keys;
    feedback_text = "";
    if ((response === "b")) {
        feedback_text = "Az \u00d6n v\u00e1lasza:\nA k\u00e9p nem marad.";
    } else {
        if ((response === "c")) {
            feedback_text = "Az \u00d6n v\u00e1lasza:\nA k\u00e9p marad.";
        } else {
            feedback_text = "Nem adott v\u00e1laszt.";
        }
    }
    
    enc_practice_feedback_image.setPos([CurrentX, CurrentY]);
    enc_practice_feedback_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    enc_practice_feedback_image.setImage(CurrentImage);
    enc_practice_feedback_text.setPos([CurrentX, (CurrentY - 0.4)]);
    enc_practice_feedback_text.setText(feedback_text);
    // keep track of which components have finished
    enc_practice_feedbackComponents = [];
    enc_practice_feedbackComponents.push(enc_practice_feedback_interior);
    enc_practice_feedbackComponents.push(enc_practice_feedback_image);
    enc_practice_feedbackComponents.push(enc_practice_feedback_text);
    
    for (const thisComponent of enc_practice_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function enc_practice_feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_practice_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_practice_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_practice_feedback_interior* updates
    if (t >= 0.0 && enc_practice_feedback_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_feedback_interior.tStart = t;  // (not accounting for frame time here)
      enc_practice_feedback_interior.frameNStart = frameN;  // exact frame index
      
      enc_practice_feedback_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_feedback_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_feedback_interior.setAutoDraw(false);
    }
    
    // *enc_practice_feedback_image* updates
    if (t >= 0.0 && enc_practice_feedback_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_feedback_image.tStart = t;  // (not accounting for frame time here)
      enc_practice_feedback_image.frameNStart = frameN;  // exact frame index
      
      enc_practice_feedback_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_feedback_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_feedback_image.setAutoDraw(false);
    }
    
    // *enc_practice_feedback_text* updates
    if (t >= 0.0 && enc_practice_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_feedback_text.tStart = t;  // (not accounting for frame time here)
      enc_practice_feedback_text.frameNStart = frameN;  // exact frame index
      
      enc_practice_feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_practice_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_practice_feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_practice_feedback'-------
    for (const thisComponent of enc_practice_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _end_practice_key_allKeys;
var end_practiceComponents;
function end_practiceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_practice'-------
    t = 0;
    end_practiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    end_practice_key.keys = undefined;
    end_practice_key.rt = undefined;
    _end_practice_key_allKeys = [];
    // keep track of which components have finished
    end_practiceComponents = [];
    end_practiceComponents.push(end_practice_text);
    end_practiceComponents.push(end_practice_key);
    end_practiceComponents.push(end_practice_continue);
    
    for (const thisComponent of end_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_practiceRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_practice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_practice_text* updates
    if (t >= 0.0 && end_practice_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_practice_text.tStart = t;  // (not accounting for frame time here)
      end_practice_text.frameNStart = frameN;  // exact frame index
      
      end_practice_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_practice_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_practice_text.setAutoDraw(false);
    }
    
    // *end_practice_key* updates
    if (t >= 1.0 && end_practice_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_practice_key.tStart = t;  // (not accounting for frame time here)
      end_practice_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_practice_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_practice_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_practice_key.clearEvents(); });
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_practice_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_practice_key.status = PsychoJS.Status.FINISHED;
  }

    if (end_practice_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_practice_key.getKeys({keyList: ['d'], waitRelease: false});
      _end_practice_key_allKeys = _end_practice_key_allKeys.concat(theseKeys);
      if (_end_practice_key_allKeys.length > 0) {
        end_practice_key.keys = _end_practice_key_allKeys[_end_practice_key_allKeys.length - 1].name;  // just the last key pressed
        end_practice_key.rt = _end_practice_key_allKeys[_end_practice_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *end_practice_continue* updates
    if (t >= 1.0 && end_practice_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_practice_continue.tStart = t;  // (not accounting for frame time here)
      end_practice_continue.frameNStart = frameN;  // exact frame index
      
      end_practice_continue.setAutoDraw(true);
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_practice_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_practice_continue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_practiceRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_practice'-------
    for (const thisComponent of end_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_practice_key.keys', end_practice_key.keys);
    if (typeof end_practice_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_practice_key.rt', end_practice_key.rt);
        routineTimer.reset();
        }
    
    end_practice_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _start_MR_trigger_allKeys;
var start_MRComponents;
function start_MRRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_MR'-------
    t = 0;
    start_MRClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    start_MR_trigger.keys = undefined;
    start_MR_trigger.rt = undefined;
    _start_MR_trigger_allKeys = [];
    // keep track of which components have finished
    start_MRComponents = [];
    start_MRComponents.push(start_MR_text);
    start_MRComponents.push(start_MR_trigger);
    
    for (const thisComponent of start_MRComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function start_MRRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'start_MR'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = start_MRClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_MR_text* updates
    if (t >= 0.0 && start_MR_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_MR_text.tStart = t;  // (not accounting for frame time here)
      start_MR_text.frameNStart = frameN;  // exact frame index
      
      start_MR_text.setAutoDraw(true);
    }

    
    // *start_MR_trigger* updates
    if (t >= 0.0 && start_MR_trigger.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_MR_trigger.tStart = t;  // (not accounting for frame time here)
      start_MR_trigger.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_MR_trigger.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_MR_trigger.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_MR_trigger.clearEvents(); });
    }

    if (start_MR_trigger.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_MR_trigger.getKeys({keyList: ['s'], waitRelease: false});
      _start_MR_trigger_allKeys = _start_MR_trigger_allKeys.concat(theseKeys);
      if (_start_MR_trigger_allKeys.length > 0) {
        start_MR_trigger.keys = _start_MR_trigger_allKeys.map((key) => key.name);  // storing all keys
        start_MR_trigger.rt = _start_MR_trigger_allKeys.map((key) => key.rt);
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_MRComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_MRRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'start_MR'-------
    for (const thisComponent of start_MRComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start_MR_trigger.keys', start_MR_trigger.keys);
    if (typeof start_MR_trigger.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_MR_trigger.rt', start_MR_trigger.rt);
        routineTimer.reset();
        }
    
    start_MR_trigger.stop();
    trigger_time = globalClock.getTime();
    thisExp.addData("trigger_time", trigger_time);
    
    // the Routine "start_MR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var selection;
var end_run_text;
var start_enc_runComponents;
function start_enc_runRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_enc_run'-------
    t = 0;
    start_enc_runClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    start = end;
    end = (start + 84);
    selection = Array.from({length: end - start}, (_, index) => index + start)
    run_counter = (run_counter + 1);
    end_run_text = "R\u00f6vid sz\u00fcnet.";
    if ((run_counter >= 2)) {
        end_run_text = "V\u00e9ge az els\u0151 feladatnak.";
    }
    
    // keep track of which components have finished
    start_enc_runComponents = [];
    start_enc_runComponents.push(start_enc_run_text);
    
    for (const thisComponent of start_enc_runComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function start_enc_runRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'start_enc_run'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = start_enc_runClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_enc_run_text* updates
    if (t >= 0.0 && start_enc_run_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_enc_run_text.tStart = t;  // (not accounting for frame time here)
      start_enc_run_text.frameNStart = frameN;  // exact frame index
      
      start_enc_run_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_enc_run_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_enc_run_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_enc_runComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_enc_runRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'start_enc_run'-------
    for (const thisComponent of start_enc_runComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _enc_fx_key_allKeys;
var enc_fxComponents;
function enc_fxRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_fx'-------
    t = 0;
    enc_fxClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    enc_fx_cross.setPos([CurrentX, CurrentY]);
    enc_fx_key.keys = undefined;
    enc_fx_key.rt = undefined;
    _enc_fx_key_allKeys = [];
    // keep track of which components have finished
    enc_fxComponents = [];
    enc_fxComponents.push(enc_fx_interior);
    enc_fxComponents.push(enc_fx_cross);
    enc_fxComponents.push(enc_fx_key);
    
    for (const thisComponent of enc_fxComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var loop_start_time;
function enc_fxRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_fx'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_fxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_fx_interior* updates
    if (t >= 0.0 && enc_fx_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_fx_interior.tStart = t;  // (not accounting for frame time here)
      enc_fx_interior.frameNStart = frameN;  // exact frame index
      
      enc_fx_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_fx_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_fx_interior.setAutoDraw(false);
    }
    
    // *enc_fx_cross* updates
    if (t >= 0.0 && enc_fx_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_fx_cross.tStart = t;  // (not accounting for frame time here)
      enc_fx_cross.frameNStart = frameN;  // exact frame index
      
      enc_fx_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_fx_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_fx_cross.setAutoDraw(false);
    }
    
    // *enc_fx_key* updates
    if (t >= 0.0 && enc_fx_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_fx_key.tStart = t;  // (not accounting for frame time here)
      enc_fx_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_fx_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_fx_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_fx_key.clearEvents(); });
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_fx_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_fx_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_fx_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_fx_key.getKeys({keyList: ['b', 'c'], waitRelease: false});
      _enc_fx_key_allKeys = _enc_fx_key_allKeys.concat(theseKeys);
      if (_enc_fx_key_allKeys.length > 0) {
        enc_fx_key.keys = _enc_fx_key_allKeys[_enc_fx_key_allKeys.length - 1].name;  // just the last key pressed
        enc_fx_key.rt = _enc_fx_key_allKeys[_enc_fx_key_allKeys.length - 1].rt;
      }
    }
    
    if (((enc_trials.thisN === 0) && (frameN === 0))) {
        loop_start_time = (globalClock.getTime() - trigger_time);
        thisExp.addData("loop_start_time", loop_start_time);
    } else {
        if ((frameN === 1)) {
            fx_start_time = (globalClock.getTime() - trigger_time);
            thisExp.addData("fx_start_time", fx_start_time);
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_fxComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_fxRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_fx'-------
    for (const thisComponent of enc_fxComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_fx_key.keys', enc_fx_key.keys);
    if (typeof enc_fx_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_fx_key.rt', enc_fx_key.rt);
        }
    
    enc_fx_key.stop();
    // the Routine "enc_fx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _enc_trial_key_allKeys;
var enc_trialComponents;
function enc_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_trial'-------
    t = 0;
    enc_trialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    w_size = psychoJS.window.size;
    
    x_size = w_size[0];
    y_size = w_size[1];
    
    scr_resolution = (x_size / y_size);
    
    enc_trial_main_image.setPos([CurrentX, CurrentY]);
    enc_trial_main_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    enc_trial_main_image.setImage(CurrentImage);
    enc_trial_key.keys = undefined;
    enc_trial_key.rt = undefined;
    _enc_trial_key_allKeys = [];
    // keep track of which components have finished
    enc_trialComponents = [];
    enc_trialComponents.push(enc_trial_interior);
    enc_trialComponents.push(enc_trial_main_image);
    enc_trialComponents.push(enc_trial_key);
    
    for (const thisComponent of enc_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var trial_start_time;
function enc_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *enc_trial_interior* updates
    if (t >= 0.0 && enc_trial_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_trial_interior.tStart = t;  // (not accounting for frame time here)
      enc_trial_interior.frameNStart = frameN;  // exact frame index
      
      enc_trial_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_trial_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_trial_interior.setAutoDraw(false);
    }
    
    // *enc_trial_main_image* updates
    if (t >= 0.0 && enc_trial_main_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_trial_main_image.tStart = t;  // (not accounting for frame time here)
      enc_trial_main_image.frameNStart = frameN;  // exact frame index
      
      enc_trial_main_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_trial_main_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_trial_main_image.setAutoDraw(false);
    }
    
    // *enc_trial_key* updates
    if (t >= 0.0 && enc_trial_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_trial_key.tStart = t;  // (not accounting for frame time here)
      enc_trial_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_trial_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_trial_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_trial_key.clearEvents(); });
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_trial_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_trial_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_trial_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_trial_key.getKeys({keyList: ['b', 'c'], waitRelease: false});
      _enc_trial_key_allKeys = _enc_trial_key_allKeys.concat(theseKeys);
      if (_enc_trial_key_allKeys.length > 0) {
        enc_trial_key.keys = _enc_trial_key_allKeys[_enc_trial_key_allKeys.length - 1].name;  // just the last key pressed
        enc_trial_key.rt = _enc_trial_key_allKeys[_enc_trial_key_allKeys.length - 1].rt;
      }
    }
    
    if ((frameN === 0)) {
        trial_start_time = (globalClock.getTime() - trigger_time);
        thisExp.addData("trial_start_time", trial_start_time);
    } else {
        if ((frameN === 1)) {
            stimulus_start_time = (globalClock.getTime() - trigger_time);
            thisExp.addData("stimulus_start_time", stimulus_start_time);
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of enc_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function enc_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_trial'-------
    for (const thisComponent of enc_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_trial_key.keys', enc_trial_key.keys);
    if (typeof enc_trial_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_trial_key.rt', enc_trial_key.rt);
        }
    
    enc_trial_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enc_run_end_key_allKeys;
var end_enc_runComponents;
function end_enc_runRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_enc_run'-------
    t = 0;
    end_enc_runClock.reset(); // clock
    frameN = -1;
    routineTimer.add(180.000000);
    // update component parameters for each repeat
    end_enc_run_text.setText(end_run_text);
    enc_run_end_key.keys = undefined;
    enc_run_end_key.rt = undefined;
    _enc_run_end_key_allKeys = [];
    // keep track of which components have finished
    end_enc_runComponents = [];
    end_enc_runComponents.push(end_enc_run_text);
    end_enc_runComponents.push(enc_run_end_key);
    end_enc_runComponents.push(enc_run_end_continue);
    
    for (const thisComponent of end_enc_runComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_enc_runRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_enc_run'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_enc_runClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_enc_run_text* updates
    if (t >= 0.0 && end_enc_run_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_enc_run_text.tStart = t;  // (not accounting for frame time here)
      end_enc_run_text.frameNStart = frameN;  // exact frame index
      
      end_enc_run_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_enc_run_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_enc_run_text.setAutoDraw(false);
    }
    
    // *enc_run_end_key* updates
    if (t >= 5 && enc_run_end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_run_end_key.tStart = t;  // (not accounting for frame time here)
      enc_run_end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_run_end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_run_end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_run_end_key.clearEvents(); });
    }

    frameRemains = 5 + 175 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_run_end_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_run_end_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_run_end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_run_end_key.getKeys({keyList: ['d'], waitRelease: false});
      _enc_run_end_key_allKeys = _enc_run_end_key_allKeys.concat(theseKeys);
      if (_enc_run_end_key_allKeys.length > 0) {
        enc_run_end_key.keys = _enc_run_end_key_allKeys[_enc_run_end_key_allKeys.length - 1].name;  // just the last key pressed
        enc_run_end_key.rt = _enc_run_end_key_allKeys[_enc_run_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *enc_run_end_continue* updates
    if (t >= 5.0 && enc_run_end_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_run_end_continue.tStart = t;  // (not accounting for frame time here)
      enc_run_end_continue.frameNStart = frameN;  // exact frame index
      
      enc_run_end_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 175 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_run_end_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_run_end_continue.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_enc_runComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_enc_runRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_enc_run'-------
    for (const thisComponent of end_enc_runComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('enc_run_end_key.keys', enc_run_end_key.keys);
    if (typeof enc_run_end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_run_end_key.rt', enc_run_end_key.rt);
        routineTimer.reset();
        }
    
    enc_run_end_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var inter_task_breakComponents;
function inter_task_breakRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'inter_task_break'-------
    t = 0;
    inter_task_breakClock.reset(); // clock
    frameN = -1;
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    inter_task_breakComponents = [];
    inter_task_breakComponents.push(inter_task_break_text);
    
    for (const thisComponent of inter_task_breakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function inter_task_breakRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'inter_task_break'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = inter_task_breakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *inter_task_break_text* updates
    if (t >= 0.0 && inter_task_break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inter_task_break_text.tStart = t;  // (not accounting for frame time here)
      inter_task_break_text.frameNStart = frameN;  // exact frame index
      
      inter_task_break_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (inter_task_break_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      inter_task_break_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of inter_task_breakComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function inter_task_breakRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'inter_task_break'-------
    for (const thisComponent of inter_task_breakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
