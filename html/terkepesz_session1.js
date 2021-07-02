/*************************** 
 * Terkepesz_Session1 Test *
 ***************************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.114, 0.31, 0.38]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'terkepesz_session1';  // from the Builder filename that created this script
let expInfo = {'online ID': ''};

// Start code blocks for 'Before Experiment'
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
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(anatomyRoutineBegin());
flowScheduler.add(anatomyRoutineEachFrame());
flowScheduler.add(anatomyRoutineEnd());
flowScheduler.add(choose_videoRoutineBegin());
flowScheduler.add(choose_videoRoutineEachFrame());
flowScheduler.add(choose_videoRoutineEnd());
flowScheduler.add(loadingRoutineBegin());
flowScheduler.add(loadingRoutineEachFrame());
flowScheduler.add(loadingRoutineEnd());
flowScheduler.add(videoRoutineBegin());
flowScheduler.add(videoRoutineEachFrame());
flowScheduler.add(videoRoutineEnd());
flowScheduler.add(resting_state_instructionRoutineBegin());
flowScheduler.add(resting_state_instructionRoutineEachFrame());
flowScheduler.add(resting_state_instructionRoutineEnd());
flowScheduler.add(resting_stateRoutineBegin());
flowScheduler.add(resting_stateRoutineEachFrame());
flowScheduler.add(resting_stateRoutineEnd());
flowScheduler.add(prepare_taskRoutineBegin());
flowScheduler.add(prepare_taskRoutineEachFrame());
flowScheduler.add(prepare_taskRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
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

function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Üdvözöljük a TTK Agyi Képalkotó Központjában!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  import * as os from 'os';
  import {colored, cprint} from 'termcolor';
  import * as colorama from 'colorama';
  os.system("color");
  colorama.init();
  win.mouseVisible = false;
  
  // Initialize components for Routine "anatomy"
  anatomyClock = new util.Clock();
  anatomy_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'anatomy_text',
    text: 'Anatómiai felvételek következnek.\n\nA felvételek közben videót vetítünk le Önnek.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  general_instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  general_instructions_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_continue',
    text: 'Ha minden rendben, nyomja le a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "choose_video"
  choose_videoClock = new util.Clock();
  choose_video_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'choose_video_text',
    text: 'Válasszon az alábbi videók közül.\n\nJobb mutatóujj: Skócia a levegőből\nJobb hüvelykujj: Afrika szépségei\n\nBal mutatóujj: Vihar\nBal hüvelykujj: Űr',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  choose_video_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "loading"
  loadingClock = new util.Clock();
  loading_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'loading_text',
    text: 'A videó betölt...',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "video"
  videoClock = new util.Clock();
  end_video_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "resting_state_instruction"
  resting_state_instructionClock = new util.Clock();
  rest_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_instructions_text',
    text: 'Most a nyugalmi mérés következik.\n\nA mérés közben egy fixációs keresztet lát majd a képernyőn.\n\nNézze ezt a keresztet. Gondolatait hagyja kalandozni.\nKérjük, közben maradjon ébren. A nyugalmi mérés 8 percig tart.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rest_instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rest_instructions_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_instructions_continue',
    text: 'Ha minden rendben nyomja le a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "resting_state"
  resting_stateClock = new util.Clock();
  fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fx_cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 0.65, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rest_end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prepare_task"
  prepare_taskClock = new util.Clock();
  prepare_task_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prepare_task_text',
    text: 'Most a feladatok következnek.\n\nHa minden rendben, nyomja le a gombot a jobb hüvelykujjával. ',
    font: 'Arial',
    units: undefined, 
    pos: [0.0, 0], height: 0.05,  wrapWidth: 0.52, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  prepare_task_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function welcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    cprint("On Screen: Welcome Message", "blue", "on_white");
    console.log("Mouse disabled on screen. Keep CMD window active!");
    cprint("Hit SPACE or -> to continue.", "red");
    
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(welcome_text);
    welcomeComponents.push(key_resp);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function welcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'welcome'-------
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 1.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['right', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of welcomeComponents)
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

function welcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'welcome'-------
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function anatomyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'anatomy'-------
    t = 0;
    anatomyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    general_instructions_key.keys = undefined;
    general_instructions_key.rt = undefined;
    _general_instructions_key_allKeys = [];
    info_text = "Anat\u00f3miai felv\u00e9telek k\u00f6vetkeznek.\nA felv\u00e9telek k\u00f6zben vide\u00f3t vet\u00edt\u00fcnk le \u00d6nnek.";
    cprint(info_text, "blue", "on_white");
    cprint("\n\nWaiting for participant response.\n\n", "yellow");
    
    // keep track of which components have finished
    anatomyComponents = [];
    anatomyComponents.push(anatomy_text);
    anatomyComponents.push(general_instructions_key);
    anatomyComponents.push(general_instructions_continue);
    
    for (const thisComponent of anatomyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function anatomyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'anatomy'-------
    // get current time
    t = anatomyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *anatomy_text* updates
    if (t >= 0.0 && anatomy_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      anatomy_text.tStart = t;  // (not accounting for frame time here)
      anatomy_text.frameNStart = frameN;  // exact frame index
      
      anatomy_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (anatomy_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      anatomy_text.setAutoDraw(false);
    }
    
    // *general_instructions_key* updates
    if (t >= 5.0 && general_instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_key.tStart = t;  // (not accounting for frame time here)
      general_instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { general_instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_key.status = PsychoJS.Status.FINISHED;
  }

    if (general_instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = general_instructions_key.getKeys({keyList: ['d'], waitRelease: false});
      _general_instructions_key_allKeys = _general_instructions_key_allKeys.concat(theseKeys);
      if (_general_instructions_key_allKeys.length > 0) {
        general_instructions_key.keys = _general_instructions_key_allKeys[_general_instructions_key_allKeys.length - 1].name;  // just the last key pressed
        general_instructions_key.rt = _general_instructions_key_allKeys[_general_instructions_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *general_instructions_continue* updates
    if (t >= 5.0 && general_instructions_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_continue.tStart = t;  // (not accounting for frame time here)
      general_instructions_continue.frameNStart = frameN;  // exact frame index
      
      general_instructions_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_continue.setAutoDraw(false);
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
    for (const thisComponent of anatomyComponents)
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

function anatomyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'anatomy'-------
    for (const thisComponent of anatomyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('general_instructions_key.keys', general_instructions_key.keys);
    if (typeof general_instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('general_instructions_key.rt', general_instructions_key.rt);
        routineTimer.reset();
        }
    
    general_instructions_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function choose_videoRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'choose_video'-------
    t = 0;
    choose_videoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    choose_video_key.keys = undefined;
    choose_video_key.rt = undefined;
    _choose_video_key_allKeys = [];
    console.log("Participant chooses video.");
    
    // keep track of which components have finished
    choose_videoComponents = [];
    choose_videoComponents.push(choose_video_text);
    choose_videoComponents.push(choose_video_key);
    
    for (const thisComponent of choose_videoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function choose_videoRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'choose_video'-------
    // get current time
    t = choose_videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *choose_video_text* updates
    if (t >= 0.0 && choose_video_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choose_video_text.tStart = t;  // (not accounting for frame time here)
      choose_video_text.frameNStart = frameN;  // exact frame index
      
      choose_video_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choose_video_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choose_video_text.setAutoDraw(false);
    }
    
    // *choose_video_key* updates
    if (t >= 1.5 && choose_video_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choose_video_key.tStart = t;  // (not accounting for frame time here)
      choose_video_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choose_video_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choose_video_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choose_video_key.clearEvents(); });
    }

    frameRemains = 1.5 + 298.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choose_video_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choose_video_key.status = PsychoJS.Status.FINISHED;
  }

    if (choose_video_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = choose_video_key.getKeys({keyList: ['a', 'd', 'c', 'b'], waitRelease: false});
      _choose_video_key_allKeys = _choose_video_key_allKeys.concat(theseKeys);
      if (_choose_video_key_allKeys.length > 0) {
        choose_video_key.keys = _choose_video_key_allKeys[_choose_video_key_allKeys.length - 1].name;  // just the last key pressed
        choose_video_key.rt = _choose_video_key_allKeys[_choose_video_key_allKeys.length - 1].rt;
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
    for (const thisComponent of choose_videoComponents)
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

function choose_videoRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'choose_video'-------
    for (const thisComponent of choose_videoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('choose_video_key.keys', choose_video_key.keys);
    if (typeof choose_video_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choose_video_key.rt', choose_video_key.rt);
        routineTimer.reset();
        }
    
    choose_video_key.stop();
    key_pressed = choose_video_key.keys;
    selected_video = "stimuli/eye_of_the_storm.mp4";
    if ((key_pressed === "d")) {
        selected_video = "stimuli/beauty_of_africa.mp4";
    } else {
        if ((key_pressed === "c")) {
            selected_video = "stimuli/scotland.mp4";
        } else {
            if ((key_pressed === "a")) {
                selected_video = "stimuli/hubble_final.mp4";
            } else {
                if ((key_pressed === "b")) {
                    selected_video = "stimuli/eye_of_the_storm.mp4";
                }
            }
        }
    }
    console.log("Video selected: ", selected_video);
    
    return Scheduler.Event.NEXT;
  };
}

function loadingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'loading'-------
    t = 0;
    loadingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    cprint("On Screen: A vide\u00f3 bet\u00f6lt...", "blue", "on_white");
    
    // keep track of which components have finished
    loadingComponents = [];
    loadingComponents.push(loading_text);
    
    for (const thisComponent of loadingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function loadingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'loading'-------
    // get current time
    t = loadingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *loading_text* updates
    if (t >= 0.0 && loading_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loading_text.tStart = t;  // (not accounting for frame time here)
      loading_text.frameNStart = frameN;  // exact frame index
      
      loading_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loading_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loading_text.setAutoDraw(false);
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
    for (const thisComponent of loadingComponents)
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

function loadingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'loading'-------
    for (const thisComponent of loadingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function videoRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'video'-------
    t = 0;
    videoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2700.000000);
    // update component parameters for each repeat
    video_fileClock = new util.Clock();
    video_file = new visual.MovieStim({
      win: psychoJS.window,
      name: 'video_file',
      units: 'pix',
      movie: selected_video,
      pos: [0, 0],
      size: [1920, 1080],
      ori: 0,
      opacity: 1,
      loop: true,
      noAudio: false,
      });
    end_video_key.keys = undefined;
    end_video_key.rt = undefined;
    _end_video_key_allKeys = [];
    n_frame = 0;
    cprint("Video playing...", "blue", "on_white");
    
    // keep track of which components have finished
    videoComponents = [];
    videoComponents.push(video_file);
    videoComponents.push(end_video_key);
    
    for (const thisComponent of videoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function videoRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'video'-------
    // get current time
    t = videoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video_file* updates
    if (t >= 0.0 && video_file.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      video_file.tStart = t;  // (not accounting for frame time here)
      video_file.frameNStart = frameN;  // exact frame index
      
      video_file.setAutoDraw(true);
      video_file.play();
    }

    frameRemains = 0.0 + 2700.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (video_file.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      video_file.setAutoDraw(false);
    }

    
    // *end_video_key* updates
    if (t >= 5.0 && end_video_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_video_key.tStart = t;  // (not accounting for frame time here)
      end_video_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_video_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_video_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_video_key.clearEvents(); });
    }

    frameRemains = 5.0 + 2695.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_video_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_video_key.status = PsychoJS.Status.FINISHED;
  }

    if (end_video_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_video_key.getKeys({keyList: ['right', 'space'], waitRelease: false});
      _end_video_key_allKeys = _end_video_key_allKeys.concat(theseKeys);
      if (_end_video_key_allKeys.length > 0) {
        end_video_key.keys = _end_video_key_allKeys[_end_video_key_allKeys.length - 1].name;  // just the last key pressed
        end_video_key.rt = _end_video_key_allKeys[_end_video_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    /* Syntax Error: Fix Python code */
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of videoComponents)
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

function videoRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'video'-------
    for (const thisComponent of videoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    video_file.stop();
    psychoJS.experiment.addData('end_video_key.keys', end_video_key.keys);
    if (typeof end_video_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_video_key.rt', end_video_key.rt);
        routineTimer.reset();
        }
    
    end_video_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function resting_state_instructionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'resting_state_instruction'-------
    t = 0;
    resting_state_instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    rest_instructions_key.keys = undefined;
    rest_instructions_key.rt = undefined;
    _rest_instructions_key_allKeys = [];
    cprint("On Screen", "blue", "on_white");
    cprint("Most a nyugalmi m\u00e9r\u00e9s k\u00f6vetkezik.", "blue", "on_white");
    cprint("A m\u00e9r\u00e9s k\u00f6zben egy fix\u00e1ci\u00f3s keresztet l\u00e1t majd a k\u00e9perny\u0151n.", "blue", "on_white");
    cprint("N\u00e9zze ezt a keresztet. Gondolatait hagyja kalandozni.", "blue", "on_white");
    cprint("K\u00e9rj\u00fck, k\u00f6zben maradjon \u00e9bren. A nyugalmi m\u00e9r\u00e9s 8 percig tart.", "blue", "on_white");
    cprint("\n\nWaiting for participant response...", "yellow");
    
    // keep track of which components have finished
    resting_state_instructionComponents = [];
    resting_state_instructionComponents.push(rest_instructions_text);
    resting_state_instructionComponents.push(rest_instructions_key);
    resting_state_instructionComponents.push(rest_instructions_continue);
    
    for (const thisComponent of resting_state_instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function resting_state_instructionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'resting_state_instruction'-------
    // get current time
    t = resting_state_instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest_instructions_text* updates
    if (t >= 0.0 && rest_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_instructions_text.tStart = t;  // (not accounting for frame time here)
      rest_instructions_text.frameNStart = frameN;  // exact frame index
      
      rest_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_instructions_text.setAutoDraw(false);
    }
    
    // *rest_instructions_key* updates
    if (t >= 10.0 && rest_instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_instructions_key.tStart = t;  // (not accounting for frame time here)
      rest_instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_instructions_key.clearEvents(); });
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_instructions_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_instructions_key.status = PsychoJS.Status.FINISHED;
  }

    if (rest_instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_instructions_key.getKeys({keyList: ['d'], waitRelease: false});
      _rest_instructions_key_allKeys = _rest_instructions_key_allKeys.concat(theseKeys);
      if (_rest_instructions_key_allKeys.length > 0) {
        rest_instructions_key.keys = _rest_instructions_key_allKeys[_rest_instructions_key_allKeys.length - 1].name;  // just the last key pressed
        rest_instructions_key.rt = _rest_instructions_key_allKeys[_rest_instructions_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rest_instructions_continue* updates
    if (t >= 10.0 && rest_instructions_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_instructions_continue.tStart = t;  // (not accounting for frame time here)
      rest_instructions_continue.frameNStart = frameN;  // exact frame index
      
      rest_instructions_continue.setAutoDraw(true);
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_instructions_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_instructions_continue.setAutoDraw(false);
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
    for (const thisComponent of resting_state_instructionComponents)
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

function resting_state_instructionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'resting_state_instruction'-------
    for (const thisComponent of resting_state_instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('rest_instructions_key.keys', rest_instructions_key.keys);
    if (typeof rest_instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_instructions_key.rt', rest_instructions_key.rt);
        routineTimer.reset();
        }
    
    rest_instructions_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function resting_stateRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'resting_state'-------
    t = 0;
    resting_stateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    rest_end_key.keys = undefined;
    rest_end_key.rt = undefined;
    _rest_end_key_allKeys = [];
    cprint("\n\nFixation cross on screen.", "blue", "on_white");
    n_frame = 0;
    
    // keep track of which components have finished
    resting_stateComponents = [];
    resting_stateComponents.push(fx_cross);
    resting_stateComponents.push(rest_end_key);
    
    for (const thisComponent of resting_stateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function resting_stateRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'resting_state'-------
    // get current time
    t = resting_stateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fx_cross* updates
    if (t >= 0.0 && fx_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fx_cross.tStart = t;  // (not accounting for frame time here)
      fx_cross.frameNStart = frameN;  // exact frame index
      
      fx_cross.setAutoDraw(true);
    }

    
    // *rest_end_key* updates
    if (t >= 5.0 && rest_end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_end_key.tStart = t;  // (not accounting for frame time here)
      rest_end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_end_key.clearEvents(); });
    }

    if (rest_end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_end_key.getKeys({keyList: ['right', 'space'], waitRelease: false});
      _rest_end_key_allKeys = _rest_end_key_allKeys.concat(theseKeys);
      if (_rest_end_key_allKeys.length > 0) {
        rest_end_key.keys = _rest_end_key_allKeys[_rest_end_key_allKeys.length - 1].name;  // just the last key pressed
        rest_end_key.rt = _rest_end_key_allKeys[_rest_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    /* Syntax Error: Fix Python code */
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of resting_stateComponents)
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

function resting_stateRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'resting_state'-------
    for (const thisComponent of resting_stateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('rest_end_key.keys', rest_end_key.keys);
    if (typeof rest_end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_end_key.rt', rest_end_key.rt);
        routineTimer.reset();
        }
    
    rest_end_key.stop();
    // the Routine "resting_state" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function prepare_taskRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prepare_task'-------
    t = 0;
    prepare_taskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    prepare_task_key.keys = undefined;
    prepare_task_key.rt = undefined;
    _prepare_task_key_allKeys = [];
    cprint("On Screen: \nMessage on screen:\nMost a feladatok k\u00f6vetkeznek.Ha minden rendben, nyomja le a gombot a jobb h\u00fcvelykujj\u00e1val.", "blue", "on_white");
    cprint("Waiting for participant response...", "yellow");
    
    // keep track of which components have finished
    prepare_taskComponents = [];
    prepare_taskComponents.push(prepare_task_text);
    prepare_taskComponents.push(prepare_task_key);
    
    for (const thisComponent of prepare_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function prepare_taskRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prepare_task'-------
    // get current time
    t = prepare_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prepare_task_text* updates
    if (t >= 0.0 && prepare_task_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prepare_task_text.tStart = t;  // (not accounting for frame time here)
      prepare_task_text.frameNStart = frameN;  // exact frame index
      
      prepare_task_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prepare_task_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prepare_task_text.setAutoDraw(false);
    }
    
    // *prepare_task_key* updates
    if (t >= 1.0 && prepare_task_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prepare_task_key.tStart = t;  // (not accounting for frame time here)
      prepare_task_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prepare_task_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prepare_task_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prepare_task_key.clearEvents(); });
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prepare_task_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prepare_task_key.status = PsychoJS.Status.FINISHED;
  }

    if (prepare_task_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = prepare_task_key.getKeys({keyList: ['d'], waitRelease: false});
      _prepare_task_key_allKeys = _prepare_task_key_allKeys.concat(theseKeys);
      if (_prepare_task_key_allKeys.length > 0) {
        prepare_task_key.keys = _prepare_task_key_allKeys[_prepare_task_key_allKeys.length - 1].name;  // just the last key pressed
        prepare_task_key.rt = _prepare_task_key_allKeys[_prepare_task_key_allKeys.length - 1].rt;
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
    for (const thisComponent of prepare_taskComponents)
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

function prepare_taskRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prepare_task'-------
    for (const thisComponent of prepare_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('prepare_task_key.keys', prepare_task_key.keys);
    if (typeof prepare_task_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prepare_task_key.rt', prepare_task_key.rt);
        routineTimer.reset();
        }
    
    prepare_task_key.stop();
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
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
