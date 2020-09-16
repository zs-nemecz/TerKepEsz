/************************* 
 * Terkepesz_Online Test *
 *************************/

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
let expName = 'terkepesz_online';  // from the Builder filename that created this script
let expInfo = {'Azonosító kód*': '', 'A vizsgálat feltételeibe beleegyezem. (igen/nem)*': '', 'Az adatkezelési feltételeket elfogadom. (igen/nem)*': ''};

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
flowScheduler.add(experiment_informationRoutineBegin());
flowScheduler.add(experiment_informationRoutineEachFrame());
flowScheduler.add(experiment_informationRoutineEnd());
const comprehension_questions_1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(comprehension_questions_1LoopBegin, comprehension_questions_1LoopScheduler);
flowScheduler.add(comprehension_questions_1LoopScheduler);
flowScheduler.add(comprehension_questions_1LoopEnd);
flowScheduler.add(data_protectionRoutineBegin());
flowScheduler.add(data_protectionRoutineEachFrame());
flowScheduler.add(data_protectionRoutineEnd());
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(lab_introductionRoutineBegin());
flowScheduler.add(lab_introductionRoutineEachFrame());
flowScheduler.add(lab_introductionRoutineEnd());
flowScheduler.add(general_instructions_1RoutineBegin());
flowScheduler.add(general_instructions_1RoutineEachFrame());
flowScheduler.add(general_instructions_1RoutineEnd());
flowScheduler.add(general_instructions_2RoutineBegin());
flowScheduler.add(general_instructions_2RoutineEachFrame());
flowScheduler.add(general_instructions_2RoutineEnd());
flowScheduler.add(general_instructions_3RoutineBegin());
flowScheduler.add(general_instructions_3RoutineEachFrame());
flowScheduler.add(general_instructions_3RoutineEnd());
flowScheduler.add(encoding_titleRoutineBegin());
flowScheduler.add(encoding_titleRoutineEachFrame());
flowScheduler.add(encoding_titleRoutineEnd());
flowScheduler.add(enc_instructions_1RoutineBegin());
flowScheduler.add(enc_instructions_1RoutineEachFrame());
flowScheduler.add(enc_instructions_1RoutineEnd());
flowScheduler.add(enc_instructions_2RoutineBegin());
flowScheduler.add(enc_instructions_2RoutineEachFrame());
flowScheduler.add(enc_instructions_2RoutineEnd());
flowScheduler.add(enc_instructions_3RoutineBegin());
flowScheduler.add(enc_instructions_3RoutineEachFrame());
flowScheduler.add(enc_instructions_3RoutineEnd());
flowScheduler.add(enc_instructions_4RoutineBegin());
flowScheduler.add(enc_instructions_4RoutineEachFrame());
flowScheduler.add(enc_instructions_4RoutineEnd());
const comprehension_questions_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(comprehension_questions_2LoopBegin, comprehension_questions_2LoopScheduler);
flowScheduler.add(comprehension_questions_2LoopScheduler);
flowScheduler.add(comprehension_questions_2LoopEnd);
flowScheduler.add(start_practiceRoutineBegin());
flowScheduler.add(start_practiceRoutineEachFrame());
flowScheduler.add(start_practiceRoutineEnd());
flowScheduler.add(encoding_titleRoutineBegin());
flowScheduler.add(encoding_titleRoutineEachFrame());
flowScheduler.add(encoding_titleRoutineEnd());
const enc_practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(enc_practice_trialsLoopBegin, enc_practice_trialsLoopScheduler);
flowScheduler.add(enc_practice_trialsLoopScheduler);
flowScheduler.add(enc_practice_trialsLoopEnd);
flowScheduler.add(end_practiceRoutineBegin());
flowScheduler.add(end_practiceRoutineEachFrame());
flowScheduler.add(end_practiceRoutineEnd());
flowScheduler.add(recognition_titleRoutineBegin());
flowScheduler.add(recognition_titleRoutineEachFrame());
flowScheduler.add(recognition_titleRoutineEnd());
flowScheduler.add(rec_instructions_1RoutineBegin());
flowScheduler.add(rec_instructions_1RoutineEachFrame());
flowScheduler.add(rec_instructions_1RoutineEnd());
flowScheduler.add(rec_instructions_2RoutineBegin());
flowScheduler.add(rec_instructions_2RoutineEachFrame());
flowScheduler.add(rec_instructions_2RoutineEnd());
flowScheduler.add(rec_instructions_3RoutineBegin());
flowScheduler.add(rec_instructions_3RoutineEachFrame());
flowScheduler.add(rec_instructions_3RoutineEnd());
flowScheduler.add(rec_instructions_4RoutineBegin());
flowScheduler.add(rec_instructions_4RoutineEachFrame());
flowScheduler.add(rec_instructions_4RoutineEnd());
flowScheduler.add(demo_startRoutineBegin());
flowScheduler.add(demo_startRoutineEachFrame());
flowScheduler.add(demo_startRoutineEnd());
const demo_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(demo_trialsLoopBegin, demo_trialsLoopScheduler);
flowScheduler.add(demo_trialsLoopScheduler);
flowScheduler.add(demo_trialsLoopEnd);
flowScheduler.add(demo_endRoutineBegin());
flowScheduler.add(demo_endRoutineEachFrame());
flowScheduler.add(demo_endRoutineEnd());
const comprehension_questions_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(comprehension_questions_3LoopBegin, comprehension_questions_3LoopScheduler);
flowScheduler.add(comprehension_questions_3LoopScheduler);
flowScheduler.add(comprehension_questions_3LoopEnd);
flowScheduler.add(start_practiceRoutineBegin());
flowScheduler.add(start_practiceRoutineEachFrame());
flowScheduler.add(start_practiceRoutineEnd());
const rec_practice_blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(rec_practice_blocksLoopBegin, rec_practice_blocksLoopScheduler);
flowScheduler.add(rec_practice_blocksLoopScheduler);
flowScheduler.add(rec_practice_blocksLoopEnd);
flowScheduler.add(end_practiceRoutineBegin());
flowScheduler.add(end_practiceRoutineEachFrame());
flowScheduler.add(end_practiceRoutineEnd());
flowScheduler.add(start_practiceRoutineBegin());
flowScheduler.add(start_practiceRoutineEachFrame());
flowScheduler.add(start_practiceRoutineEnd());
const full_practceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(full_practceLoopBegin, full_practceLoopScheduler);
flowScheduler.add(full_practceLoopScheduler);
flowScheduler.add(full_practceLoopEnd);
flowScheduler.add(end_practiceRoutineBegin());
flowScheduler.add(end_practiceRoutineEachFrame());
flowScheduler.add(end_practiceRoutineEnd());
const sessionLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(sessionLoopBegin, sessionLoopScheduler);
flowScheduler.add(sessionLoopScheduler);
flowScheduler.add(sessionLoopEnd);
const comprehension_endLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(comprehension_endLoopBegin, comprehension_endLoopScheduler);
flowScheduler.add(comprehension_endLoopScheduler);
flowScheduler.add(comprehension_endLoopEnd);
flowScheduler.add(end_experimentRoutineBegin());
flowScheduler.add(end_experimentRoutineEachFrame());
flowScheduler.add(end_experimentRoutineEnd());
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


var experiment_informationClock;
var experiment_information_text;
var experiment_information_key;
var experiment_information_continue;
var proceed;
var consent;
var dataprotection;
var consent_ok;
var data_ok;
var tables;
var trial_table;
var enc_table;
var rec_table;
var comprehension_questionClock;
var comprehension_question_text;
var comprehension_question_answers;
var comprehension_key;
var comprehension_feedbackClock;
var comprehension_feedback_text;
var comprehension_repeatClock;
var comprehension_continue_key;
var comprehension_continue_text;
var comprehension_repeat_text;
var data_protectionClock;
var consentClock;
var lab_introductionClock;
var lab_thanks;
var lab_key;
var lab_introduction_continue;
var lab_members;
var general_instructions_1Clock;
var general_instructions_text;
var general_instructions_key;
var general_instructions_continue;
var general_instructions_2Clock;
var general_instructions_text_2;
var general_instructions_key_2;
var general_instructions_continue_2;
var general_instructions_3Clock;
var general_instructions_text_3;
var general_instructions_key_3;
var general_instructions_continue_3;
var encoding_titleClock;
var encoding_title_text;
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
var enc_instructions_2_text_2;
var enc_instructions_2_image_2;
var enc_instructions_2_key_2;
var instructions_2_continue_2;
var enc_instructions_4Clock;
var enc_instructions_3_text;
var enc_instructions_3_key;
var enc_instructions_3_continue;
var start_practiceClock;
var start_practice_text;
var practice_block_startClock;
var practice_end;
var step;
var start_practice_block;
var enc_fxClock;
var w_size;
var x_size;
var y_size;
var scr_resolution;
var enc_fx_interior;
var enc_fx_cross;
var enc_fx_key;
var enc_fx_text_block;
var enc_fx_instructions_text;
var enc_trialClock;
var enc_trial_interior;
var enc_trial_main_image;
var enc_trial_key;
var enc_trial_text_block;
var enc_trial_instructions_text;
var enc_practice_feedbackClock;
var enc_practice_feedback_interior;
var enc_practice_feedback_image;
var enc_practice_feedback_text;
var enc_practice_feedback_block;
var end_practiceClock;
var end_practice_text;
var end_practice_key;
var end_practice_continue;
var coming_up_next_text;
var recognition_titleClock;
var start_recognition_text;
var rec_instructions_1Clock;
var rec_instructions_1_text;
var rec_instructions_1_key;
var rec_instructions_1_continue;
var rec_instructions_2Clock;
var rec_instructions2_text;
var rec_instructions_2_key;
var rec_instructions_2_continue;
var rec_instruction_2_title;
var rec_instructions_3Clock;
var rec_instrauction_3_text;
var rec_instructions_3_key;
var rec_instructions_3_continue;
var rec_instruction_3_title;
var rec_instructions_4Clock;
var rec_instructions_4_text;
var rec_instructions_4_key;
var rec_instructions_4_continue;
var demo_startClock;
var demo_start_text;
var demoClock;
var demo_interior;
var demo_main_image;
var demo_image;
var demo_text;
var demo_key;
var demo_continue;
var demo_endClock;
var demo_end_text;
var demo_end_key;
var demo_end_continue;
var rec_fxClock;
var rec_fx_interior;
var rec_fx_cross;
var rec_fx_key;
var rec_fx_text_block;
var rec_fx_instructions_text;
var rec_trialClock;
var rec_trial_interior;
var rec_trial_main_image;
var rec_trial_key;
var rec_trial_text_block;
var rec_trial_instructions_text;
var rec_practice_feedbackClock;
var rec_practice_feedback_text;
var block_titleClock;
var block_title_text;
var start_runClock;
var run_counter;
var start_enc_run_text;
var init_blocksClock;
var rec_end;
var start_rec_block_text;
var enc_end;
var end_runClock;
var end_enc_run_text;
var enc_run_end_key;
var inter_task_breakClock;
var block_name_selection;
var inter_task_break_continue;
var inter_task_break_text;
var inter_task_break_key;
var end_experimentClock;
var end_experiment_text;
var code;
var end_experiment_code;
var end_experiment_continue;
var end_experiment_key;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "experiment_information"
  experiment_informationClock = new util.Clock();
  experiment_information_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'experiment_information_text',
    text: 'Kérjük, figyelmesen olvassa végig az alábbi instrukciókat!\n\nA vizsgálathoz használjon asztali számítógépet vagy laptopot. A vizsgálat nem végezhető el mobil eszközön, például okostelefonon vagy táblagépen. A feladatok elvégzéséhez szüksége lesz működő billentyűzetre és stabil internet kapcsolatra. Az optimális eredmény elérése érdekében Google Chrome, Firefox vagy Safari böngésző használata javasolt. Kérjük, használja a teljes képernyő módot.\nA kísérlet teljes körű, zavartalan figyelmet igényel. A vizsgálat elvégzése 50-60 percet vesz igénybe. Bizonyosodjon meg róla, hogy elég időt tud szánni a vizsgálatra. Ügyeljen arra, hogy telefont, vagy más eszközöket közben ne használjon, és kerülje a másokkal való interakciót.\n\nA vizsgálat két feladattípusból áll, melyek során absztrakt képeket kell kiválogatnia a megadott szempontok szerint. A feladattípusokat 8 perces körökben, váltakozva fogja elvégezni. A körök között lesz lehetősége rövid pihenőt tartani. \n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  experiment_information_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  experiment_information_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'experiment_information_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  proceed = false;
  consent = expInfo["A vizsg\u00e1lat felt\u00e9teleibe beleegyezem. (igen/nem)*"];
  dataprotection = expInfo["Az adatkezel\u00e9si felt\u00e9teleket elfogadom. (igen/nem)*"];
  consent_ok = false;
  data_ok = false;
  if (((((consent === "igen") || (consent === "i")) || (consent === "Igen")) || (consent === "I"))) {
      consent_ok = true;
  }
  if (((((dataprotection === "igen") || (dataprotection === "i")) || (dataprotection === "Igen")) || (dataprotection === "I"))) {
      data_ok = true;
  }
  if ((consent_ok & data_ok)) {
      proceed = true;
  }
  if ((! proceed)) {
      core.quit();
  }
  
  tables = ["0","1","2"];
  trial_table = tables[Math.floor(Math.random() * tables.length)];
  
  enc_table = (("stimuli_tables/encoding_trials_" + trial_table) + ".csv");
  rec_table = (("stimuli_tables/recognition_trials_" + trial_table) + ".csv");
  // Initialize components for Routine "comprehension_question"
  comprehension_questionClock = new util.Clock();
  comprehension_question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  comprehension_question_answers = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_answers',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_feedback"
  comprehension_feedbackClock = new util.Clock();
  comprehension_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "comprehension_repeat"
  comprehension_repeatClock = new util.Clock();
  comprehension_continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  comprehension_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_continue_text',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_repeat_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_repeat_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "data_protection"
  data_protectionClock = new util.Clock();
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  // Initialize components for Routine "lab_introduction"
  lab_introductionClock = new util.Clock();
  lab_thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'lab_thanks',
    text: 'Köszönjük, hogy hozzájárul kutatócsoportunk munkájához azzal, hogy részt vesz vizsgálatunkban!\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  lab_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  lab_introduction_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'lab_introduction_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  lab_members = new visual.ImageStim({
    win : psychoJS.window,
    name : 'lab_members', units : 'norm', 
    image : 'stimuli/lab_members.jpg', mask : undefined,
    ori : 0, pos : [0, (- 0.3704)], size : [0.9458, 1.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "general_instructions_1"
  general_instructions_1Clock = new util.Clock();
  general_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_text',
    text: 'A vizsgálat kétféle feladattípusból áll.\n\nAz első feladattípus a Galériaberendezés. Ebben a feladatban képeket kell beválogatnia egy modern művészeti galériába. \n\nA második feladattípus a Képfelismerés. Ebben a feladatban azt kell eldöntenie, a bemutatott képeket látta-e a megelőző Galériaberendezés feladat során. \n\nA vizsgálatot 6 körre osztottuk, úgy, hogy egy Képfelismerés feladatot Önnek mindig a közvetlenül megelőző Galériaberendezés feladat alapján kell elvégeznie. \n\nEgy kör 8 percet vesz igénybe, a körök között rövid (maximum 2 perces) szünetet tud tartani. A harmadik kör után tarthat egy hosszabb (maximum 10 perces) szünetet. \n\n\n\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  general_instructions_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  general_instructions_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "general_instructions_2"
  general_instructions_2Clock = new util.Clock();
  general_instructions_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_text_2',
    text: "Mindkét feladatnak két típusa van: 'Kép' és 'Hely'.\n\nGalériaberendezés:\nHa az alfeladat neve 'Kép', akkor arról kell döntést hoznia, hogy a bemutatott kép ki legyen-e állítva a következő kiállításon.\nHa az alfeladat neve 'Hely', akkor azt kell eldöntenie, a bemutatt kép az aktuálisan jelzett helyen legyen-e kiállítva.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  general_instructions_key_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  general_instructions_continue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_continue_2',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "general_instructions_3"
  general_instructions_3Clock = new util.Clock();
  general_instructions_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_text_3',
    text: "Képfelismerés:\nHa az alfeladat neve 'Kép', akkor arra kell választ adnia, a bemutatott kép pontosan megegyezik-e a Galériaberendezés feladatban látot képek egyikével. \nHa az alfeladat neve 'Hely', akkor a képek pozíciójáról kell döntenie: a képernyő ugyanezen pontján látta korábban a bemutatott képet?\n\nA vizsgálatot 6 körre osztottuk, úgy, hogy egy Képfelismerés blokkot Önnek mindig a közvetlenül megelőző Galériaberendezés blokk alapján kell elvégeznie. \nA sorrend lehet például:\n\n'Kép' Galériaberendezés -> 'Kép' Képfelismerés\n'Hely' Galériaberendezés -> 'Hely' Képfelismerés\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  general_instructions_key_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  general_instructions_continue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'general_instructions_continue_3',
    text: 'Most részletesebben bemutatjuk Önnek a Galériaberendezés feladatot. \nA folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "encoding_title"
  encoding_titleClock = new util.Clock();
  encoding_title_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'encoding_title_text',
    text: 'Galéria berendezés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "enc_instructions_1"
  enc_instructions_1Clock = new util.Clock();
  enc_instructions_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_1_text',
    text: 'Ön ennek a modern képgalériának a kurátora. \n\nA legújabb kiállításra a vártnál több kép érkezett.\nKurátorként az Ön feladata lesz eldönteni, mely képeket válogatjuk be a kiállított darabok közé, és hogy a mások által beválogatott képek illeszkednek-e a galéria adott pontjára.\n\nAz Ön ideje nagyon drága a galériának, így a döntésre egy-egy képről csak 3 másodperce lesz.',
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
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
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
    text: "Ez a kiállítóterem, nézze meg figyelmesen. \n\nA feladat során a képek a falra vetítve jelennek meg. A képek előtt egy keresztet fog látni, ami jelzi a képek pontos helyét.\n\nA 'Kép' nevű alfeladat alatt döntse el a képekről, hogy ki legyenek-e állítva a galériában. \n\nA beválogatott képek száma nincsen korlátozva. Minden egyes képről Ön dönt. \n\nHa több képet válogat be, mint amennyi a galériába fér, akkor a képeket az év során felváltva állítjuk ki.\n",
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), 0], height: 0.03,  wrapWidth: 0.52, ori: 0,
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
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "enc_instructions_3"
  enc_instructions_3Clock = new util.Clock();
  enc_instructions_2_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_2_text_2',
    text: "A 'Hely' nevű alfeladat alatt azt döntse el, a bemutatott kép maradhat-e a galéria adott pontján.\nEzeket a képeket mindenképp kiállítjuk, itt csak a képek helyéről tud dönteni. \n\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ. ",
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.35), 0], height: 0.03,  wrapWidth: 0.52, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  enc_instructions_2_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_instructions_2_image_2', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0.4427, 0], size : [0.7604, 0.8185],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_instructions_2_key_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instructions_2_continue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_2_continue_2',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "enc_instructions_4"
  enc_instructions_4Clock = new util.Clock();
  enc_instructions_3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_instructions_3_text',
    text: "A 'Kép' alfeladat alatt a 'J' billentyűvel jelölje azokat a képeket, amelyeket beválogat a kiállításra. \n\nAz 'F' billentyűvel jelölje a képeket, amelyeket nem válogat be a kiállításra.\n\n\nA 'Hely' nevű alfeladatban a 'J' billentyűvel jelölje azokat a képeket, amelyek maradhatnak a galéria adott pontján. \n\nAz 'F' billentyűvel jelölje a képeket, amelyek nem maradhatnak a galéria adott pontján.\n\nMost a Galériaberendezés gyakorlása következik. \n",
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
    text: 'Ha készen áll a gyakorlásra, nyomja le a jobb nyilat.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "comprehension_question"
  comprehension_questionClock = new util.Clock();
  comprehension_question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  comprehension_question_answers = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_answers',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_feedback"
  comprehension_feedbackClock = new util.Clock();
  comprehension_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "comprehension_repeat"
  comprehension_repeatClock = new util.Clock();
  comprehension_continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  comprehension_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_continue_text',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_repeat_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_repeat_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
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
  
  // Initialize components for Routine "encoding_title"
  encoding_titleClock = new util.Clock();
  encoding_title_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'encoding_title_text',
    text: 'Galéria berendezés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_block_start"
  practice_block_startClock = new util.Clock();
  practice_end = 0;
  step = 1;
  
  start_practice_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_practice_block',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "enc_fx"
  enc_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  enc_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  enc_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  enc_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
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
  
  enc_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
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
  
  enc_practice_feedback_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_practice_feedback_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "end_practice"
  end_practiceClock = new util.Clock();
  end_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_practice_text',
    text: 'Ez volt a gyakorlás.',
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
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  coming_up_next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'coming_up_next_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "recognition_title"
  recognition_titleClock = new util.Clock();
  start_recognition_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_recognition_text',
    text: 'Képfelismerés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "rec_instructions_1"
  rec_instructions_1Clock = new util.Clock();
  rec_instructions_1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_1_text',
    text: 'A Képfelismerés feladatban ismét absztrakt képeket fog látni, és ezekről kell eldöntenie, látta-e őket a megelőző Galériaberendezés feladataban, és hogy ugyanott látta-e őket.\n\nA feladatot két alfeladatra bontottuk. Az egyikben a képekről, a másikban a képek pozíciójáról kell döntenie.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rec_instructions_1_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_instructions_1_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_1_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "rec_instructions_2"
  rec_instructions_2Clock = new util.Clock();
  rec_instructions2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions2_text',
    text: "A 'Kép' nevű alfeladatban azt kell eldöntenie, látta-e már ezeket a képeket a megelőző Galériaberendezés blokkban.\n\nKét csoportba oszthatóak a megjelenő képek:\n - Régi: Ezek a képek pontosan megegyeznek a 'Galériaberendezés' megelőző sorozatában látott képek egyikével.\n - Új: Képek, amelyek nem jelentek meg a 'Galériaberendezés' feladatban. Ezek a képek lehetnek hasonlóak a korábban látottakhoz.\n\nAz Ön feladata, hogy eldöntse, melyik kép ugyanaz, mint a 'Galéria berendezés' feladatban, és melyik új. \nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nDöntését így jelölje:\nRégi - F\nÚj - J",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: 1, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rec_instructions_2_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_instructions_2_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_2_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rec_instruction_2_title = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instruction_2_title',
    text: "'Kép' alfeladat",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "rec_instructions_3"
  rec_instructions_3Clock = new util.Clock();
  rec_instrauction_3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instrauction_3_text',
    text: "A 'Hely' nevű alfeladatban azt kell eldöntenie, a képek a képernyő ugyanazon pontján jelennek-e meg, mint a megelőző Galériaberendezés sorozatban.\nEbben az alfeladatban minden kép pontos mása annak, amit a Galériaberendezés alatt látott. \n\nA helyek azonban két csoportba oszthatóak:\n - Régi: Pontosan ugyanitt jelent meg ez a kép a Galériaberendezés feladatban.\n - Új: Egy másik helyen jelent meg ez a kép a Galériaberendezés feladatban. Ez a hely lehet közeli az eredeti helyhez.\n\nAz Ön feladata, hogy eldöntse, melyik kép jelent meg ugyanott, és melyik új helyen.\nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nA döntését így jelölje:\nRégi - F\nÚj - J",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: 1, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rec_instructions_3_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_instructions_3_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_3_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rec_instruction_3_title = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instruction_3_title',
    text: "'Hely' alfeladat",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "rec_instructions_4"
  rec_instructions_4Clock = new util.Clock();
  rec_instructions_4_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_4_text',
    text: "A következőkben pár példával mutatjuk be Önnek, milyen hasonlóak lehetnek az új képek és helyek.\n\nA bemutatóban elsőként egy, a Galériaberendezés gyakorlása során már látott képet/helyet mutatunk Önnek, 'Régi' felirattal. \nA régi képet/helyet mindig egy új kép/hely követi a bemutatóban, 'Új' felirattal.\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rec_instructions_4_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_instructions_4_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_instructions_4_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "demo_start"
  demo_startClock = new util.Clock();
  demo_start_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_start_text',
    text: 'Kezdődik a bemutató...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "demo"
  demoClock = new util.Clock();
  demo_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'demo_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  demo_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'demo_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  demo_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'demo_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  demo_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.025), 0.45], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  demo_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  demo_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "demo_end"
  demo_endClock = new util.Clock();
  demo_end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_end_text',
    text: 'Ez volt a bemutató. Most a Képfelismerés gyakorlása következik.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  demo_end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  demo_end_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'demo_end_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "comprehension_question"
  comprehension_questionClock = new util.Clock();
  comprehension_question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  comprehension_question_answers = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_answers',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_feedback"
  comprehension_feedbackClock = new util.Clock();
  comprehension_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "comprehension_repeat"
  comprehension_repeatClock = new util.Clock();
  comprehension_continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  comprehension_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_continue_text',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_repeat_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_repeat_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
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
  
  // Initialize components for Routine "practice_block_start"
  practice_block_startClock = new util.Clock();
  practice_end = 0;
  step = 1;
  
  start_practice_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_practice_block',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "rec_fx"
  rec_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  rec_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rec_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  rec_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "rec_trial"
  rec_trialClock = new util.Clock();
  rec_trial_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  rec_trial_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_trial_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  rec_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "rec_practice_feedback"
  rec_practice_feedbackClock = new util.Clock();
  rec_practice_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_practice_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_practice"
  end_practiceClock = new util.Clock();
  end_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_practice_text',
    text: 'Ez volt a gyakorlás.',
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
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  coming_up_next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'coming_up_next_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
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
  
  // Initialize components for Routine "practice_block_start"
  practice_block_startClock = new util.Clock();
  practice_end = 0;
  step = 1;
  
  start_practice_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_practice_block',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "enc_fx"
  enc_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  enc_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  enc_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  enc_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
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
  
  enc_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
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
  
  enc_practice_feedback_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_practice_feedback_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "recognition_title"
  recognition_titleClock = new util.Clock();
  start_recognition_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_recognition_text',
    text: 'Képfelismerés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "block_title"
  block_titleClock = new util.Clock();
  block_title_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'block_title_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "rec_fx"
  rec_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  rec_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rec_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  rec_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "rec_trial"
  rec_trialClock = new util.Clock();
  rec_trial_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  rec_trial_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_trial_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  rec_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "rec_practice_feedback"
  rec_practice_feedbackClock = new util.Clock();
  rec_practice_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_practice_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_practice"
  end_practiceClock = new util.Clock();
  end_practice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_practice_text',
    text: 'Ez volt a gyakorlás.',
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
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  coming_up_next_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'coming_up_next_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "start_run"
  start_runClock = new util.Clock();
  run_counter = 0;
  
  start_enc_run_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_enc_run_text',
    text: 'Kezdődik a feladat...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "encoding_title"
  encoding_titleClock = new util.Clock();
  encoding_title_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'encoding_title_text',
    text: 'Galéria berendezés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "init_blocks"
  init_blocksClock = new util.Clock();
  rec_end = 0;
  start_rec_block_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_rec_block_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  enc_end = 0;
  
  // Initialize components for Routine "enc_fx"
  enc_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  enc_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'enc_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  enc_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  enc_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  enc_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_fx_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
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
  
  enc_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  enc_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'enc_trial_instructions_text',
    text: '[F - Nem marad]      [J - Marad]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "recognition_title"
  recognition_titleClock = new util.Clock();
  start_recognition_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_recognition_text',
    text: 'Képfelismerés',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "block_title"
  block_titleClock = new util.Clock();
  block_title_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'block_title_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "rec_fx"
  rec_fxClock = new util.Clock();
  w_size = psychoJS.window.size;
  
  x_size = w_size[0];
  y_size = w_size[1];
  
  scr_resolution = (x_size / y_size);
  
  rec_fx_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_fx_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_fx_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_cross',
    text: '+',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  rec_fx_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_fx_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  rec_fx_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_fx_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "rec_trial"
  rec_trialClock = new util.Clock();
  rec_trial_interior = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_interior', units : 'norm', 
    image : 'stimuli/GalleryInterior.png', mask : undefined,
    ori : 0, pos : [0, (- 0)], size : [2.0, 2.0],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  rec_trial_main_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rec_trial_main_image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  rec_trial_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_trial_text_block = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_text_block',
    text: 'default text',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.87], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  rec_trial_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rec_trial_instructions_text',
    text: '[F - Régi]      [J - Új]',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.833)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "comprehension_question"
  comprehension_questionClock = new util.Clock();
  comprehension_question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  comprehension_question_answers = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_answers',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_feedback"
  comprehension_feedbackClock = new util.Clock();
  comprehension_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "comprehension_repeat"
  comprehension_repeatClock = new util.Clock();
  comprehension_continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  comprehension_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_continue_text',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_repeat_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_repeat_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "end_run"
  end_runClock = new util.Clock();
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
  
  // Initialize components for Routine "inter_task_break"
  inter_task_breakClock = new util.Clock();
  block_name_selection = [1, 51, 101];
  
  inter_task_break_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'inter_task_break_continue',
    text: 'A folytatáshoz nyomja le a jobb nyilat.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  inter_task_break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'inter_task_break_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  inter_task_break_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_question"
  comprehension_questionClock = new util.Clock();
  comprehension_question_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  comprehension_question_answers = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_question_answers',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "comprehension_feedback"
  comprehension_feedbackClock = new util.Clock();
  comprehension_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_feedback_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "comprehension_repeat"
  comprehension_repeatClock = new util.Clock();
  comprehension_continue_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  comprehension_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_continue_text',
    text: 'A folytatáshoz nyomja le a jobb nyilat. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  comprehension_repeat_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'comprehension_repeat_text',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "end_experiment"
  end_experimentClock = new util.Clock();
  end_experiment_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_experiment_text',
    text: 'Köszönjük a részvételt!\n\nJegyezze fel az alábbi kódot, amellyel a részvételét igazolja:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  code = Math.floor(100000 + Math.random() * 900000)
  
  end_experiment_code = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_experiment_code',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  end_experiment_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_experiment_continue',
    text: 'A jobb nyíl lenyomásával megjelenik a vizsgálat végét jelző üzenet. Ezt fogadja el az OK gombbal, majd átirányítjuk egy felületre, ahol a kód megadásával igazolni tudja a részvételét.\nProbléma esetén írjon nekünk a terkep@ttk.hu email címen. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  end_experiment_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _experiment_information_key_allKeys;
var experiment_informationComponents;
function experiment_informationRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'experiment_information'-------
    t = 0;
    experiment_informationClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    experiment_information_key.keys = undefined;
    experiment_information_key.rt = undefined;
    _experiment_information_key_allKeys = [];
    // keep track of which components have finished
    experiment_informationComponents = [];
    experiment_informationComponents.push(experiment_information_text);
    experiment_informationComponents.push(experiment_information_key);
    experiment_informationComponents.push(experiment_information_continue);
    
    experiment_informationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
var continueRoutine;
function experiment_informationRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'experiment_information'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = experiment_informationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *experiment_information_text* updates
    if (t >= 0.0 && experiment_information_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      experiment_information_text.tStart = t;  // (not accounting for frame time here)
      experiment_information_text.frameNStart = frameN;  // exact frame index
      
      experiment_information_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (experiment_information_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      experiment_information_text.setAutoDraw(false);
    }
    
    // *experiment_information_key* updates
    if (t >= 10.0 && experiment_information_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      experiment_information_key.tStart = t;  // (not accounting for frame time here)
      experiment_information_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { experiment_information_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { experiment_information_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { experiment_information_key.clearEvents(); });
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (experiment_information_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      experiment_information_key.status = PsychoJS.Status.FINISHED;
  }

    if (experiment_information_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = experiment_information_key.getKeys({keyList: ['right'], waitRelease: false});
      _experiment_information_key_allKeys = _experiment_information_key_allKeys.concat(theseKeys);
      if (_experiment_information_key_allKeys.length > 0) {
        experiment_information_key.keys = _experiment_information_key_allKeys[_experiment_information_key_allKeys.length - 1].name;  // just the last key pressed
        experiment_information_key.rt = _experiment_information_key_allKeys[_experiment_information_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *experiment_information_continue* updates
    if (t >= 10.0 && experiment_information_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      experiment_information_continue.tStart = t;  // (not accounting for frame time here)
      experiment_information_continue.frameNStart = frameN;  // exact frame index
      
      experiment_information_continue.setAutoDraw(true);
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (experiment_information_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      experiment_information_continue.setAutoDraw(false);
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
    experiment_informationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function experiment_informationRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'experiment_information'-------
    experiment_informationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('experiment_information_key.keys', experiment_information_key.keys);
    if (typeof experiment_information_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('experiment_information_key.rt', experiment_information_key.rt);
        routineTimer.reset();
        }
    
    experiment_information_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var comprehension_questions_1;
var currentLoop;
function comprehension_questions_1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  comprehension_questions_1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/comprehension_questions.xlsx', '0:2'),
    seed: undefined, name: 'comprehension_questions_1'
  });
  psychoJS.experiment.addLoop(comprehension_questions_1); // add the loop to the experiment
  currentLoop = comprehension_questions_1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  comprehension_questions_1.forEach(function() {
    const snapshot = comprehension_questions_1.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(comprehension_questionRoutineBegin(snapshot));
    thisScheduler.add(comprehension_questionRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_questionRoutineEnd(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineBegin(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEnd(snapshot));
    thisScheduler.add(comprehension_repeatRoutineBegin(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function comprehension_questions_1LoopEnd() {
  psychoJS.experiment.removeLoop(comprehension_questions_1);

  return Scheduler.Event.NEXT;
}


var comprehension_questions_2;
function comprehension_questions_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  comprehension_questions_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/comprehension_questions.xlsx', '2:4'),
    seed: undefined, name: 'comprehension_questions_2'
  });
  psychoJS.experiment.addLoop(comprehension_questions_2); // add the loop to the experiment
  currentLoop = comprehension_questions_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  comprehension_questions_2.forEach(function() {
    const snapshot = comprehension_questions_2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(comprehension_questionRoutineBegin(snapshot));
    thisScheduler.add(comprehension_questionRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_questionRoutineEnd(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineBegin(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEnd(snapshot));
    thisScheduler.add(comprehension_repeatRoutineBegin(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function comprehension_questions_2LoopEnd() {
  psychoJS.experiment.removeLoop(comprehension_questions_2);

  return Scheduler.Event.NEXT;
}


var enc_practice_trials;
function enc_practice_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_practice_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/encoding_practice_trials.csv', '1,4'),
    seed: undefined, name: 'enc_practice_trials'
  });
  psychoJS.experiment.addLoop(enc_practice_trials); // add the loop to the experiment
  currentLoop = enc_practice_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  enc_practice_trials.forEach(function() {
    const snapshot = enc_practice_trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practice_block_startRoutineBegin(snapshot));
    thisScheduler.add(practice_block_startRoutineEachFrame(snapshot));
    thisScheduler.add(practice_block_startRoutineEnd(snapshot));
    const enc_practice_blockLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(enc_practice_blockLoopBegin, enc_practice_blockLoopScheduler);
    thisScheduler.add(enc_practice_blockLoopScheduler);
    thisScheduler.add(enc_practice_blockLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var enc_practice_block;
function enc_practice_blockLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_practice_block = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/encoding_practice_trials.csv', practice_selection),
    seed: undefined, name: 'enc_practice_block'
  });
  psychoJS.experiment.addLoop(enc_practice_block); // add the loop to the experiment
  currentLoop = enc_practice_block;  // we're now the current loop

  // Schedule all the trials in the trialList:
  enc_practice_block.forEach(function() {
    const snapshot = enc_practice_block.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(enc_fxRoutineBegin(snapshot));
    thisScheduler.add(enc_fxRoutineEachFrame(snapshot));
    thisScheduler.add(enc_fxRoutineEnd(snapshot));
    thisScheduler.add(enc_trialRoutineBegin(snapshot));
    thisScheduler.add(enc_trialRoutineEachFrame(snapshot));
    thisScheduler.add(enc_trialRoutineEnd(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineBegin(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function enc_practice_blockLoopEnd() {
  psychoJS.experiment.removeLoop(enc_practice_block);

  return Scheduler.Event.NEXT;
}


function enc_practice_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(enc_practice_trials);

  return Scheduler.Event.NEXT;
}


var demo_trials;
function demo_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  demo_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'stimuli_tables/stimuli_demo.xlsx',
    seed: undefined, name: 'demo_trials'
  });
  psychoJS.experiment.addLoop(demo_trials); // add the loop to the experiment
  currentLoop = demo_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  demo_trials.forEach(function() {
    const snapshot = demo_trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(demoRoutineBegin(snapshot));
    thisScheduler.add(demoRoutineEachFrame(snapshot));
    thisScheduler.add(demoRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function demo_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(demo_trials);

  return Scheduler.Event.NEXT;
}


var comprehension_questions_3;
function comprehension_questions_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  comprehension_questions_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/comprehension_questions.xlsx', '6:8'),
    seed: undefined, name: 'comprehension_questions_3'
  });
  psychoJS.experiment.addLoop(comprehension_questions_3); // add the loop to the experiment
  currentLoop = comprehension_questions_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  comprehension_questions_3.forEach(function() {
    const snapshot = comprehension_questions_3.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(comprehension_questionRoutineBegin(snapshot));
    thisScheduler.add(comprehension_questionRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_questionRoutineEnd(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineBegin(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEnd(snapshot));
    thisScheduler.add(comprehension_repeatRoutineBegin(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function comprehension_questions_3LoopEnd() {
  psychoJS.experiment.removeLoop(comprehension_questions_3);

  return Scheduler.Event.NEXT;
}


var rec_practice_blocks;
function rec_practice_blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  rec_practice_blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/recognition_practice_trials.csv', '1,4'),
    seed: undefined, name: 'rec_practice_blocks'
  });
  psychoJS.experiment.addLoop(rec_practice_blocks); // add the loop to the experiment
  currentLoop = rec_practice_blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rec_practice_blocks.forEach(function() {
    const snapshot = rec_practice_blocks.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practice_block_startRoutineBegin(snapshot));
    thisScheduler.add(practice_block_startRoutineEachFrame(snapshot));
    thisScheduler.add(practice_block_startRoutineEnd(snapshot));
    const rec_practice_trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(rec_practice_trialsLoopBegin, rec_practice_trialsLoopScheduler);
    thisScheduler.add(rec_practice_trialsLoopScheduler);
    thisScheduler.add(rec_practice_trialsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var rec_practice_trials;
function rec_practice_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  rec_practice_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/recognition_practice_trials.csv', practice_selection),
    seed: undefined, name: 'rec_practice_trials'
  });
  psychoJS.experiment.addLoop(rec_practice_trials); // add the loop to the experiment
  currentLoop = rec_practice_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rec_practice_trials.forEach(function() {
    const snapshot = rec_practice_trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(rec_fxRoutineBegin(snapshot));
    thisScheduler.add(rec_fxRoutineEachFrame(snapshot));
    thisScheduler.add(rec_fxRoutineEnd(snapshot));
    thisScheduler.add(rec_trialRoutineBegin(snapshot));
    thisScheduler.add(rec_trialRoutineEachFrame(snapshot));
    thisScheduler.add(rec_trialRoutineEnd(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineBegin(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function rec_practice_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(rec_practice_trials);

  return Scheduler.Event.NEXT;
}


function rec_practice_blocksLoopEnd() {
  psychoJS.experiment.removeLoop(rec_practice_blocks);

  return Scheduler.Event.NEXT;
}


var full_practce;
function full_practceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  full_practce = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/recognition_full_practice_trials.csv', '1, 4'),
    seed: undefined, name: 'full_practce'
  });
  psychoJS.experiment.addLoop(full_practce); // add the loop to the experiment
  currentLoop = full_practce;  // we're now the current loop

  // Schedule all the trials in the trialList:
  full_practce.forEach(function() {
    const snapshot = full_practce.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(practice_block_startRoutineBegin(snapshot));
    thisScheduler.add(practice_block_startRoutineEachFrame(snapshot));
    thisScheduler.add(practice_block_startRoutineEnd(snapshot));
    const enc_full_practiceLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(enc_full_practiceLoopBegin, enc_full_practiceLoopScheduler);
    thisScheduler.add(enc_full_practiceLoopScheduler);
    thisScheduler.add(enc_full_practiceLoopEnd);
    thisScheduler.add(recognition_titleRoutineBegin(snapshot));
    thisScheduler.add(recognition_titleRoutineEachFrame(snapshot));
    thisScheduler.add(recognition_titleRoutineEnd(snapshot));
    thisScheduler.add(block_titleRoutineBegin(snapshot));
    thisScheduler.add(block_titleRoutineEachFrame(snapshot));
    thisScheduler.add(block_titleRoutineEnd(snapshot));
    const rec_full_practiceLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(rec_full_practiceLoopBegin, rec_full_practiceLoopScheduler);
    thisScheduler.add(rec_full_practiceLoopScheduler);
    thisScheduler.add(rec_full_practiceLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var enc_full_practice;
function enc_full_practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_full_practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/encoding_full_practice_trials.csv', practice_selection),
    seed: undefined, name: 'enc_full_practice'
  });
  psychoJS.experiment.addLoop(enc_full_practice); // add the loop to the experiment
  currentLoop = enc_full_practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  enc_full_practice.forEach(function() {
    const snapshot = enc_full_practice.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(enc_fxRoutineBegin(snapshot));
    thisScheduler.add(enc_fxRoutineEachFrame(snapshot));
    thisScheduler.add(enc_fxRoutineEnd(snapshot));
    thisScheduler.add(enc_trialRoutineBegin(snapshot));
    thisScheduler.add(enc_trialRoutineEachFrame(snapshot));
    thisScheduler.add(enc_trialRoutineEnd(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineBegin(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(enc_practice_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function enc_full_practiceLoopEnd() {
  psychoJS.experiment.removeLoop(enc_full_practice);

  return Scheduler.Event.NEXT;
}


var rec_full_practice;
function rec_full_practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  rec_full_practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/recognition_full_practice_trials.csv', practice_selection),
    seed: undefined, name: 'rec_full_practice'
  });
  psychoJS.experiment.addLoop(rec_full_practice); // add the loop to the experiment
  currentLoop = rec_full_practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rec_full_practice.forEach(function() {
    const snapshot = rec_full_practice.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(rec_fxRoutineBegin(snapshot));
    thisScheduler.add(rec_fxRoutineEachFrame(snapshot));
    thisScheduler.add(rec_fxRoutineEnd(snapshot));
    thisScheduler.add(rec_trialRoutineBegin(snapshot));
    thisScheduler.add(rec_trialRoutineEachFrame(snapshot));
    thisScheduler.add(rec_trialRoutineEnd(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineBegin(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(rec_practice_feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function rec_full_practiceLoopEnd() {
  psychoJS.experiment.removeLoop(rec_full_practice);

  return Scheduler.Event.NEXT;
}


function full_practceLoopEnd() {
  psychoJS.experiment.removeLoop(full_practce);

  return Scheduler.Event.NEXT;
}


var session;
function sessionLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  session = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'session'
  });
  psychoJS.experiment.addLoop(session); // add the loop to the experiment
  currentLoop = session;  // we're now the current loop

  // Schedule all the trials in the trialList:
  session.forEach(function() {
    const snapshot = session.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const runLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(runLoopBegin, runLoopScheduler);
    thisScheduler.add(runLoopScheduler);
    thisScheduler.add(runLoopEnd);
    thisScheduler.add(inter_task_breakRoutineBegin(snapshot));
    thisScheduler.add(inter_task_breakRoutineEachFrame(snapshot));
    thisScheduler.add(inter_task_breakRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var run;
function runLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  run = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, enc_table, block_name_selection),
    seed: undefined, name: 'run'
  });
  psychoJS.experiment.addLoop(run); // add the loop to the experiment
  currentLoop = run;  // we're now the current loop

  // Schedule all the trials in the trialList:
  run.forEach(function() {
    const snapshot = run.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(start_runRoutineBegin(snapshot));
    thisScheduler.add(start_runRoutineEachFrame(snapshot));
    thisScheduler.add(start_runRoutineEnd(snapshot));
    thisScheduler.add(encoding_titleRoutineBegin(snapshot));
    thisScheduler.add(encoding_titleRoutineEachFrame(snapshot));
    thisScheduler.add(encoding_titleRoutineEnd(snapshot));
    thisScheduler.add(init_blocksRoutineBegin(snapshot));
    thisScheduler.add(init_blocksRoutineEachFrame(snapshot));
    thisScheduler.add(init_blocksRoutineEnd(snapshot));
    const enc_trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(enc_trialsLoopBegin, enc_trialsLoopScheduler);
    thisScheduler.add(enc_trialsLoopScheduler);
    thisScheduler.add(enc_trialsLoopEnd);
    thisScheduler.add(recognition_titleRoutineBegin(snapshot));
    thisScheduler.add(recognition_titleRoutineEachFrame(snapshot));
    thisScheduler.add(recognition_titleRoutineEnd(snapshot));
    thisScheduler.add(block_titleRoutineBegin(snapshot));
    thisScheduler.add(block_titleRoutineEachFrame(snapshot));
    thisScheduler.add(block_titleRoutineEnd(snapshot));
    const rec_trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(rec_trialsLoopBegin, rec_trialsLoopScheduler);
    thisScheduler.add(rec_trialsLoopScheduler);
    thisScheduler.add(rec_trialsLoopEnd);
    const comprehension_question_4LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(comprehension_question_4LoopBegin, comprehension_question_4LoopScheduler);
    thisScheduler.add(comprehension_question_4LoopScheduler);
    thisScheduler.add(comprehension_question_4LoopEnd);
    thisScheduler.add(end_runRoutineBegin(snapshot));
    thisScheduler.add(end_runRoutineEachFrame(snapshot));
    thisScheduler.add(end_runRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var enc_trials;
function enc_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  enc_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, enc_table, enc_selection),
    seed: undefined, name: 'enc_trials'
  });
  psychoJS.experiment.addLoop(enc_trials); // add the loop to the experiment
  currentLoop = enc_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  enc_trials.forEach(function() {
    const snapshot = enc_trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(enc_fxRoutineBegin(snapshot));
    thisScheduler.add(enc_fxRoutineEachFrame(snapshot));
    thisScheduler.add(enc_fxRoutineEnd(snapshot));
    thisScheduler.add(enc_trialRoutineBegin(snapshot));
    thisScheduler.add(enc_trialRoutineEachFrame(snapshot));
    thisScheduler.add(enc_trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function enc_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(enc_trials);

  return Scheduler.Event.NEXT;
}


var rec_trials;
function rec_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  rec_trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, rec_table, rec_selection),
    seed: undefined, name: 'rec_trials'
  });
  psychoJS.experiment.addLoop(rec_trials); // add the loop to the experiment
  currentLoop = rec_trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  rec_trials.forEach(function() {
    const snapshot = rec_trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(rec_fxRoutineBegin(snapshot));
    thisScheduler.add(rec_fxRoutineEachFrame(snapshot));
    thisScheduler.add(rec_fxRoutineEnd(snapshot));
    thisScheduler.add(rec_trialRoutineBegin(snapshot));
    thisScheduler.add(rec_trialRoutineEachFrame(snapshot));
    thisScheduler.add(rec_trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function rec_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(rec_trials);

  return Scheduler.Event.NEXT;
}


var comprehension_question_4;
function comprehension_question_4LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  comprehension_question_4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/comprehension_questions.xlsx', '4:6'),
    seed: undefined, name: 'comprehension_question_4'
  });
  psychoJS.experiment.addLoop(comprehension_question_4); // add the loop to the experiment
  currentLoop = comprehension_question_4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  comprehension_question_4.forEach(function() {
    const snapshot = comprehension_question_4.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(comprehension_questionRoutineBegin(snapshot));
    thisScheduler.add(comprehension_questionRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_questionRoutineEnd(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineBegin(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEnd(snapshot));
    thisScheduler.add(comprehension_repeatRoutineBegin(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function comprehension_question_4LoopEnd() {
  psychoJS.experiment.removeLoop(comprehension_question_4);

  return Scheduler.Event.NEXT;
}


function runLoopEnd() {
  psychoJS.experiment.removeLoop(run);

  return Scheduler.Event.NEXT;
}


function sessionLoopEnd() {
  psychoJS.experiment.removeLoop(session);

  return Scheduler.Event.NEXT;
}


var comprehension_end;
function comprehension_endLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  comprehension_end = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'stimuli_tables/comprehension_questions.xlsx', '8:11'),
    seed: undefined, name: 'comprehension_end'
  });
  psychoJS.experiment.addLoop(comprehension_end); // add the loop to the experiment
  currentLoop = comprehension_end;  // we're now the current loop

  // Schedule all the trials in the trialList:
  comprehension_end.forEach(function() {
    const snapshot = comprehension_end.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(comprehension_questionRoutineBegin(snapshot));
    thisScheduler.add(comprehension_questionRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_questionRoutineEnd(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineBegin(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_feedbackRoutineEnd(snapshot));
    thisScheduler.add(comprehension_repeatRoutineBegin(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEachFrame(snapshot));
    thisScheduler.add(comprehension_repeatRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function comprehension_endLoopEnd() {
  psychoJS.experiment.removeLoop(comprehension_end);

  return Scheduler.Event.NEXT;
}


var _comprehension_key_allKeys;
var comprehension_questionComponents;
function comprehension_questionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'comprehension_question'-------
    t = 0;
    comprehension_questionClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    comprehension_question_text.setText(Question);
    comprehension_question_answers.setText(Answer);
    comprehension_key.keys = undefined;
    comprehension_key.rt = undefined;
    _comprehension_key_allKeys = [];
    // keep track of which components have finished
    comprehension_questionComponents = [];
    comprehension_questionComponents.push(comprehension_question_text);
    comprehension_questionComponents.push(comprehension_question_answers);
    comprehension_questionComponents.push(comprehension_key);
    
    comprehension_questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function comprehension_questionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'comprehension_question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = comprehension_questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comprehension_question_text* updates
    if (t >= 0.0 && comprehension_question_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_question_text.tStart = t;  // (not accounting for frame time here)
      comprehension_question_text.frameNStart = frameN;  // exact frame index
      
      comprehension_question_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_question_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_question_text.setAutoDraw(false);
    }
    
    // *comprehension_question_answers* updates
    if (t >= 0.0 && comprehension_question_answers.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_question_answers.tStart = t;  // (not accounting for frame time here)
      comprehension_question_answers.frameNStart = frameN;  // exact frame index
      
      comprehension_question_answers.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_question_answers.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_question_answers.setAutoDraw(false);
    }
    
    // *comprehension_key* updates
    if (t >= 1.0 && comprehension_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_key.tStart = t;  // (not accounting for frame time here)
      comprehension_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { comprehension_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { comprehension_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { comprehension_key.clearEvents(); });
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_key.status = PsychoJS.Status.FINISHED;
  }

    if (comprehension_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = comprehension_key.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _comprehension_key_allKeys = _comprehension_key_allKeys.concat(theseKeys);
      if (_comprehension_key_allKeys.length > 0) {
        comprehension_key.keys = _comprehension_key_allKeys[0].name;  // just the first key pressed
        comprehension_key.rt = _comprehension_key_allKeys[0].rt;
        // was this correct?
        if (comprehension_key.keys == CorrectResponse) {
            comprehension_key.corr = 1;
        } else {
            comprehension_key.corr = 0;
        }
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
    comprehension_questionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function comprehension_questionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'comprehension_question'-------
    comprehension_questionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (comprehension_key.keys === undefined) {
      if (['None','none',undefined].includes(CorrectResponse)) {
         comprehension_key.corr = 1;  // correct non-response
      } else {
         comprehension_key.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('comprehension_key.keys', comprehension_key.keys);
    psychoJS.experiment.addData('comprehension_key.corr', comprehension_key.corr);
    if (typeof comprehension_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('comprehension_key.rt', comprehension_key.rt);
        routineTimer.reset();
        }
    
    comprehension_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var comprehension_repeat;
var comprehension_feedback;
var comprehension_feedbackComponents;
function comprehension_feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'comprehension_feedback'-------
    t = 0;
    comprehension_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    comprehension_repeat = 300.0;
    comprehension_feedback = IncorrectAnswer;
    if ((comprehension_key.corr === 1)) {
        comprehension_repeat = 0.0;
        comprehension_feedback = CorrectAnswer;
    }
    
    comprehension_feedback_text.setText(comprehension_feedback);
    // keep track of which components have finished
    comprehension_feedbackComponents = [];
    comprehension_feedbackComponents.push(comprehension_feedback_text);
    
    comprehension_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function comprehension_feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'comprehension_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = comprehension_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comprehension_feedback_text* updates
    if (t >= 0 && comprehension_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_feedback_text.tStart = t;  // (not accounting for frame time here)
      comprehension_feedback_text.frameNStart = frameN;  // exact frame index
      
      comprehension_feedback_text.setAutoDraw(true);
    }

    frameRemains = 0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_feedback_text.setAutoDraw(false);
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
    comprehension_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function comprehension_feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'comprehension_feedback'-------
    comprehension_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _comprehension_continue_key_allKeys;
var comprehension_repeatComponents;
function comprehension_repeatRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'comprehension_repeat'-------
    t = 0;
    comprehension_repeatClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    comprehension_continue_key.keys = undefined;
    comprehension_continue_key.rt = undefined;
    _comprehension_continue_key_allKeys = [];
    comprehension_repeat_text.setPos([0, 0]);
    comprehension_repeat_text.setText(InfoRepeated);
    // keep track of which components have finished
    comprehension_repeatComponents = [];
    comprehension_repeatComponents.push(comprehension_continue_key);
    comprehension_repeatComponents.push(comprehension_continue_text);
    comprehension_repeatComponents.push(comprehension_repeat_text);
    
    comprehension_repeatComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function comprehension_repeatRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'comprehension_repeat'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = comprehension_repeatClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comprehension_continue_key* updates
    if (t >= 1.0 && comprehension_continue_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_continue_key.tStart = t;  // (not accounting for frame time here)
      comprehension_continue_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { comprehension_continue_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { comprehension_continue_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { comprehension_continue_key.clearEvents(); });
    }

    frameRemains = 1.0 + comprehension_repeat - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_continue_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_continue_key.status = PsychoJS.Status.FINISHED;
  }

    if (comprehension_continue_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = comprehension_continue_key.getKeys({keyList: ['right'], waitRelease: false});
      _comprehension_continue_key_allKeys = _comprehension_continue_key_allKeys.concat(theseKeys);
      if (_comprehension_continue_key_allKeys.length > 0) {
        comprehension_continue_key.keys = _comprehension_continue_key_allKeys[_comprehension_continue_key_allKeys.length - 1].name;  // just the last key pressed
        comprehension_continue_key.rt = _comprehension_continue_key_allKeys[_comprehension_continue_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *comprehension_continue_text* updates
    if (t >= 1.0 && comprehension_continue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_continue_text.tStart = t;  // (not accounting for frame time here)
      comprehension_continue_text.frameNStart = frameN;  // exact frame index
      
      comprehension_continue_text.setAutoDraw(true);
    }

    frameRemains = 1.0 + comprehension_repeat - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_continue_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_continue_text.setAutoDraw(false);
    }
    
    // *comprehension_repeat_text* updates
    if (t >= 0.0 && comprehension_repeat_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comprehension_repeat_text.tStart = t;  // (not accounting for frame time here)
      comprehension_repeat_text.frameNStart = frameN;  // exact frame index
      
      comprehension_repeat_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + comprehension_repeat - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (comprehension_repeat_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      comprehension_repeat_text.setAutoDraw(false);
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
    comprehension_repeatComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function comprehension_repeatRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'comprehension_repeat'-------
    comprehension_repeatComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('comprehension_continue_key.keys', comprehension_continue_key.keys);
    if (typeof comprehension_continue_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('comprehension_continue_key.rt', comprehension_continue_key.rt);
        routineTimer.reset();
        }
    
    comprehension_continue_key.stop();
    // the Routine "comprehension_repeat" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var data_protectionComponents;
function data_protectionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'data_protection'-------
    t = 0;
    data_protectionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    data_protectionComponents = [];
    
    data_protectionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function data_protectionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'data_protection'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = data_protectionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    data_protectionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function data_protectionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'data_protection'-------
    data_protectionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "data_protection" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var consentComponents;
function consentRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'consent'-------
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    consentComponents = [];
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function consentRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'consent'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'consent'-------
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _lab_key_allKeys;
var lab_introductionComponents;
function lab_introductionRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'lab_introduction'-------
    t = 0;
    lab_introductionClock.reset(); // clock
    frameN = -1;
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    lab_key.keys = undefined;
    lab_key.rt = undefined;
    _lab_key_allKeys = [];
    // keep track of which components have finished
    lab_introductionComponents = [];
    lab_introductionComponents.push(lab_thanks);
    lab_introductionComponents.push(lab_key);
    lab_introductionComponents.push(lab_introduction_continue);
    lab_introductionComponents.push(lab_members);
    
    lab_introductionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function lab_introductionRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'lab_introduction'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = lab_introductionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *lab_thanks* updates
    if (t >= 0.0 && lab_thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lab_thanks.tStart = t;  // (not accounting for frame time here)
      lab_thanks.frameNStart = frameN;  // exact frame index
      
      lab_thanks.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lab_thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lab_thanks.setAutoDraw(false);
    }
    
    // *lab_key* updates
    if (t >= 0.0 && lab_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lab_key.tStart = t;  // (not accounting for frame time here)
      lab_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { lab_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { lab_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { lab_key.clearEvents(); });
    }

    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lab_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lab_key.status = PsychoJS.Status.FINISHED;
  }

    if (lab_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = lab_key.getKeys({keyList: ['right'], waitRelease: false});
      _lab_key_allKeys = _lab_key_allKeys.concat(theseKeys);
      if (_lab_key_allKeys.length > 0) {
        lab_key.keys = _lab_key_allKeys[_lab_key_allKeys.length - 1].name;  // just the last key pressed
        lab_key.rt = _lab_key_allKeys[_lab_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *lab_introduction_continue* updates
    if (t >= 1.0 && lab_introduction_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lab_introduction_continue.tStart = t;  // (not accounting for frame time here)
      lab_introduction_continue.frameNStart = frameN;  // exact frame index
      
      lab_introduction_continue.setAutoDraw(true);
    }

    frameRemains = 1.0 + 119.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lab_introduction_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lab_introduction_continue.setAutoDraw(false);
    }
    
    // *lab_members* updates
    if (t >= 0.0 && lab_members.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lab_members.tStart = t;  // (not accounting for frame time here)
      lab_members.frameNStart = frameN;  // exact frame index
      
      lab_members.setAutoDraw(true);
    }

    frameRemains = 0.0 + 120.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lab_members.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lab_members.setAutoDraw(false);
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
    lab_introductionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lab_introductionRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'lab_introduction'-------
    lab_introductionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('lab_key.keys', lab_key.keys);
    if (typeof lab_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('lab_key.rt', lab_key.rt);
        routineTimer.reset();
        }
    
    lab_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _general_instructions_key_allKeys;
var general_instructions_1Components;
function general_instructions_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'general_instructions_1'-------
    t = 0;
    general_instructions_1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    general_instructions_key.keys = undefined;
    general_instructions_key.rt = undefined;
    _general_instructions_key_allKeys = [];
    // keep track of which components have finished
    general_instructions_1Components = [];
    general_instructions_1Components.push(general_instructions_text);
    general_instructions_1Components.push(general_instructions_key);
    general_instructions_1Components.push(general_instructions_continue);
    
    general_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function general_instructions_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'general_instructions_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = general_instructions_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *general_instructions_text* updates
    if (t >= 0.0 && general_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_text.tStart = t;  // (not accounting for frame time here)
      general_instructions_text.frameNStart = frameN;  // exact frame index
      
      general_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_text.setAutoDraw(false);
    }
    
    // *general_instructions_key* updates
    if (t >= 10.0 && general_instructions_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_key.tStart = t;  // (not accounting for frame time here)
      general_instructions_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { general_instructions_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key.clearEvents(); });
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_key.status = PsychoJS.Status.FINISHED;
  }

    if (general_instructions_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = general_instructions_key.getKeys({keyList: ['right'], waitRelease: false});
      _general_instructions_key_allKeys = _general_instructions_key_allKeys.concat(theseKeys);
      if (_general_instructions_key_allKeys.length > 0) {
        general_instructions_key.keys = _general_instructions_key_allKeys[_general_instructions_key_allKeys.length - 1].name;  // just the last key pressed
        general_instructions_key.rt = _general_instructions_key_allKeys[_general_instructions_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *general_instructions_continue* updates
    if (t >= 10.0 && general_instructions_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_continue.tStart = t;  // (not accounting for frame time here)
      general_instructions_continue.frameNStart = frameN;  // exact frame index
      
      general_instructions_continue.setAutoDraw(true);
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    general_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function general_instructions_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'general_instructions_1'-------
    general_instructions_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('general_instructions_key.keys', general_instructions_key.keys);
    if (typeof general_instructions_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('general_instructions_key.rt', general_instructions_key.rt);
        routineTimer.reset();
        }
    
    general_instructions_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _general_instructions_key_2_allKeys;
var general_instructions_2Components;
function general_instructions_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'general_instructions_2'-------
    t = 0;
    general_instructions_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    general_instructions_key_2.keys = undefined;
    general_instructions_key_2.rt = undefined;
    _general_instructions_key_2_allKeys = [];
    // keep track of which components have finished
    general_instructions_2Components = [];
    general_instructions_2Components.push(general_instructions_text_2);
    general_instructions_2Components.push(general_instructions_key_2);
    general_instructions_2Components.push(general_instructions_continue_2);
    
    general_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function general_instructions_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'general_instructions_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = general_instructions_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *general_instructions_text_2* updates
    if (t >= 0.0 && general_instructions_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_text_2.tStart = t;  // (not accounting for frame time here)
      general_instructions_text_2.frameNStart = frameN;  // exact frame index
      
      general_instructions_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_text_2.setAutoDraw(false);
    }
    
    // *general_instructions_key_2* updates
    if (t >= 10.0 && general_instructions_key_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_key_2.tStart = t;  // (not accounting for frame time here)
      general_instructions_key_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { general_instructions_key_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key_2.clearEvents(); });
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_key_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_key_2.status = PsychoJS.Status.FINISHED;
  }

    if (general_instructions_key_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = general_instructions_key_2.getKeys({keyList: ['right'], waitRelease: false});
      _general_instructions_key_2_allKeys = _general_instructions_key_2_allKeys.concat(theseKeys);
      if (_general_instructions_key_2_allKeys.length > 0) {
        general_instructions_key_2.keys = _general_instructions_key_2_allKeys[_general_instructions_key_2_allKeys.length - 1].name;  // just the last key pressed
        general_instructions_key_2.rt = _general_instructions_key_2_allKeys[_general_instructions_key_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *general_instructions_continue_2* updates
    if (t >= 10.0 && general_instructions_continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_continue_2.tStart = t;  // (not accounting for frame time here)
      general_instructions_continue_2.frameNStart = frameN;  // exact frame index
      
      general_instructions_continue_2.setAutoDraw(true);
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_continue_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_continue_2.setAutoDraw(false);
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
    general_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function general_instructions_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'general_instructions_2'-------
    general_instructions_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('general_instructions_key_2.keys', general_instructions_key_2.keys);
    if (typeof general_instructions_key_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('general_instructions_key_2.rt', general_instructions_key_2.rt);
        routineTimer.reset();
        }
    
    general_instructions_key_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var _general_instructions_key_3_allKeys;
var general_instructions_3Components;
function general_instructions_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'general_instructions_3'-------
    t = 0;
    general_instructions_3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    general_instructions_key_3.keys = undefined;
    general_instructions_key_3.rt = undefined;
    _general_instructions_key_3_allKeys = [];
    // keep track of which components have finished
    general_instructions_3Components = [];
    general_instructions_3Components.push(general_instructions_text_3);
    general_instructions_3Components.push(general_instructions_key_3);
    general_instructions_3Components.push(general_instructions_continue_3);
    
    general_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function general_instructions_3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'general_instructions_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = general_instructions_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *general_instructions_text_3* updates
    if (t >= 0.0 && general_instructions_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_text_3.tStart = t;  // (not accounting for frame time here)
      general_instructions_text_3.frameNStart = frameN;  // exact frame index
      
      general_instructions_text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_text_3.setAutoDraw(false);
    }
    
    // *general_instructions_key_3* updates
    if (t >= 10.0 && general_instructions_key_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_key_3.tStart = t;  // (not accounting for frame time here)
      general_instructions_key_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { general_instructions_key_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { general_instructions_key_3.clearEvents(); });
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_key_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_key_3.status = PsychoJS.Status.FINISHED;
  }

    if (general_instructions_key_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = general_instructions_key_3.getKeys({keyList: ['right'], waitRelease: false});
      _general_instructions_key_3_allKeys = _general_instructions_key_3_allKeys.concat(theseKeys);
      if (_general_instructions_key_3_allKeys.length > 0) {
        general_instructions_key_3.keys = _general_instructions_key_3_allKeys[_general_instructions_key_3_allKeys.length - 1].name;  // just the last key pressed
        general_instructions_key_3.rt = _general_instructions_key_3_allKeys[_general_instructions_key_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *general_instructions_continue_3* updates
    if (t >= 10.0 && general_instructions_continue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      general_instructions_continue_3.tStart = t;  // (not accounting for frame time here)
      general_instructions_continue_3.frameNStart = frameN;  // exact frame index
      
      general_instructions_continue_3.setAutoDraw(true);
    }

    frameRemains = 10.0 + 290.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (general_instructions_continue_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      general_instructions_continue_3.setAutoDraw(false);
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
    general_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function general_instructions_3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'general_instructions_3'-------
    general_instructions_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('general_instructions_key_3.keys', general_instructions_key_3.keys);
    if (typeof general_instructions_key_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('general_instructions_key_3.rt', general_instructions_key_3.rt);
        routineTimer.reset();
        }
    
    general_instructions_key_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var encoding_titleComponents;
function encoding_titleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'encoding_title'-------
    t = 0;
    encoding_titleClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    encoding_titleComponents = [];
    encoding_titleComponents.push(encoding_title_text);
    
    encoding_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function encoding_titleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'encoding_title'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = encoding_titleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *encoding_title_text* updates
    if (t >= 0.0 && encoding_title_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encoding_title_text.tStart = t;  // (not accounting for frame time here)
      encoding_title_text.frameNStart = frameN;  // exact frame index
      
      encoding_title_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (encoding_title_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      encoding_title_text.setAutoDraw(false);
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
    encoding_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function encoding_titleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'encoding_title'-------
    encoding_titleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    enc_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
      let theseKeys = enc_instructions_1_key.getKeys({keyList: ['right'], waitRelease: false});
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
    enc_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_instructions_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    enc_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
      let theseKeys = enc_instructions_2_key.getKeys({keyList: ['right'], waitRelease: false});
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
    enc_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_instructions_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('enc_instructions_2_key.keys', enc_instructions_2_key.keys);
    if (typeof enc_instructions_2_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_2_key.rt', enc_instructions_2_key.rt);
        routineTimer.reset();
        }
    
    enc_instructions_2_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enc_instructions_2_key_2_allKeys;
var enc_instructions_3Components;
function enc_instructions_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_instructions_3'-------
    t = 0;
    enc_instructions_3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    enc_instructions_2_key_2.keys = undefined;
    enc_instructions_2_key_2.rt = undefined;
    _enc_instructions_2_key_2_allKeys = [];
    // keep track of which components have finished
    enc_instructions_3Components = [];
    enc_instructions_3Components.push(enc_instructions_2_text_2);
    enc_instructions_3Components.push(enc_instructions_2_image_2);
    enc_instructions_3Components.push(enc_instructions_2_key_2);
    enc_instructions_3Components.push(instructions_2_continue_2);
    
    enc_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    
    // *enc_instructions_2_text_2* updates
    if (t >= 0.0 && enc_instructions_2_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_text_2.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_text_2.frameNStart = frameN;  // exact frame index
      
      enc_instructions_2_text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_text_2.setAutoDraw(false);
    }
    
    // *enc_instructions_2_image_2* updates
    if (t >= 0.0 && enc_instructions_2_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_image_2.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_image_2.frameNStart = frameN;  // exact frame index
      
      enc_instructions_2_image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_image_2.setAutoDraw(false);
    }
    
    // *enc_instructions_2_key_2* updates
    if (t >= 5.0 && enc_instructions_2_key_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_instructions_2_key_2.tStart = t;  // (not accounting for frame time here)
      enc_instructions_2_key_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_instructions_2_key_2.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_instructions_2_key_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_instructions_2_key_2.status = PsychoJS.Status.FINISHED;
  }

    if (enc_instructions_2_key_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_instructions_2_key_2.getKeys({keyList: ['right'], waitRelease: false});
      _enc_instructions_2_key_2_allKeys = _enc_instructions_2_key_2_allKeys.concat(theseKeys);
      if (_enc_instructions_2_key_2_allKeys.length > 0) {
        enc_instructions_2_key_2.keys = _enc_instructions_2_key_2_allKeys[_enc_instructions_2_key_2_allKeys.length - 1].name;  // just the last key pressed
        enc_instructions_2_key_2.rt = _enc_instructions_2_key_2_allKeys[_enc_instructions_2_key_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instructions_2_continue_2* updates
    if (t >= 5.0 && instructions_2_continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_2_continue_2.tStart = t;  // (not accounting for frame time here)
      instructions_2_continue_2.frameNStart = frameN;  // exact frame index
      
      instructions_2_continue_2.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (instructions_2_continue_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      instructions_2_continue_2.setAutoDraw(false);
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
    enc_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_instructions_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('enc_instructions_2_key_2.keys', enc_instructions_2_key_2.keys);
    if (typeof enc_instructions_2_key_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_2_key_2.rt', enc_instructions_2_key_2.rt);
        routineTimer.reset();
        }
    
    enc_instructions_2_key_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var _enc_instructions_3_key_allKeys;
var enc_instructions_4Components;
function enc_instructions_4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'enc_instructions_4'-------
    t = 0;
    enc_instructions_4Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    enc_instructions_3_key.keys = undefined;
    enc_instructions_3_key.rt = undefined;
    _enc_instructions_3_key_allKeys = [];
    // keep track of which components have finished
    enc_instructions_4Components = [];
    enc_instructions_4Components.push(enc_instructions_3_text);
    enc_instructions_4Components.push(enc_instructions_3_key);
    enc_instructions_4Components.push(enc_instructions_3_continue);
    
    enc_instructions_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function enc_instructions_4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'enc_instructions_4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = enc_instructions_4Clock.getTime();
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
      let theseKeys = enc_instructions_3_key.getKeys({keyList: ['right'], waitRelease: false});
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
    enc_instructions_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var coming_up_text;
function enc_instructions_4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'enc_instructions_4'-------
    enc_instructions_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('enc_instructions_3_key.keys', enc_instructions_3_key.keys);
    if (typeof enc_instructions_3_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_instructions_3_key.rt', enc_instructions_3_key.rt);
        routineTimer.reset();
        }
    
    enc_instructions_3_key.stop();
    coming_up_text = "Most a K\u00e9pfelismer\u00e9s feladat bemutat\u00e1sa k\u00f6vetkezik.";
    
    return Scheduler.Event.NEXT;
  };
}


var practice_start;
var start_practiceComponents;
function start_practiceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_practice'-------
    t = 0;
    start_practiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    practice_start = 0;
    practice_end = 0;
    
    // keep track of which components have finished
    start_practiceComponents = [];
    start_practiceComponents.push(start_practice_text);
    
    start_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    start_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    start_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var practice_selection;
var block_name;
var practice_block_startComponents;
function practice_block_startRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practice_block_start'-------
    t = 0;
    practice_block_startClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    practice_start = practice_end;
    practice_end = (practice_start + 3);
    practice_selection = Array.from({length: practice_end - practice_start}, (_, index) => index + practice_start);
    block_name = "";
    if ((TrialType === "OBJ")) {
        block_name = "K\u00e9p";
    } else {
        if ((TrialType === "LOC")) {
            block_name = "Hely";
        } else {
            block_name = "Block Unknown";
        }
    }
    
    start_practice_block.setText(block_name);
    // keep track of which components have finished
    practice_block_startComponents = [];
    practice_block_startComponents.push(start_practice_block);
    
    practice_block_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function practice_block_startRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practice_block_start'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practice_block_startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_practice_block* updates
    if (t >= 0.0 && start_practice_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_practice_block.tStart = t;  // (not accounting for frame time here)
      start_practice_block.frameNStart = frameN;  // exact frame index
      
      start_practice_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_practice_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_practice_block.setAutoDraw(false);
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
    practice_block_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_block_startRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practice_block_start'-------
    practice_block_startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    w_size = psychoJS.window.size;
    
    x_size = w_size[0];
    y_size = w_size[1];
    
    scr_resolution = (x_size / y_size);
    
    enc_fx_cross.setPos([CurrentX, CurrentY]);
    enc_fx_key.keys = undefined;
    enc_fx_key.rt = undefined;
    _enc_fx_key_allKeys = [];
    enc_fx_text_block.setText(block_name);
    // keep track of which components have finished
    enc_fxComponents = [];
    enc_fxComponents.push(enc_fx_interior);
    enc_fxComponents.push(enc_fx_cross);
    enc_fxComponents.push(enc_fx_key);
    enc_fxComponents.push(enc_fx_text_block);
    enc_fxComponents.push(enc_fx_instructions_text);
    
    enc_fxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


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
      let theseKeys = enc_fx_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _enc_fx_key_allKeys = _enc_fx_key_allKeys.concat(theseKeys);
      if (_enc_fx_key_allKeys.length > 0) {
        enc_fx_key.keys = _enc_fx_key_allKeys[_enc_fx_key_allKeys.length - 1].name;  // just the last key pressed
        enc_fx_key.rt = _enc_fx_key_allKeys[_enc_fx_key_allKeys.length - 1].rt;
      }
    }
    
    
    // *enc_fx_text_block* updates
    if (t >= 0.0 && enc_fx_text_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_fx_text_block.tStart = t;  // (not accounting for frame time here)
      enc_fx_text_block.frameNStart = frameN;  // exact frame index
      
      enc_fx_text_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_fx_text_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_fx_text_block.setAutoDraw(false);
    }
    
    // *enc_fx_instructions_text* updates
    if (t >= 0.0 && enc_fx_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_fx_instructions_text.tStart = t;  // (not accounting for frame time here)
      enc_fx_instructions_text.frameNStart = frameN;  // exact frame index
      
      enc_fx_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_fx_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_fx_instructions_text.setAutoDraw(false);
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
    enc_fxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_fxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    enc_trial_text_block.setText(block_name);
    // keep track of which components have finished
    enc_trialComponents = [];
    enc_trialComponents.push(enc_trial_interior);
    enc_trialComponents.push(enc_trial_main_image);
    enc_trialComponents.push(enc_trial_key);
    enc_trialComponents.push(enc_trial_text_block);
    enc_trialComponents.push(enc_trial_instructions_text);
    
    enc_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


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
      let theseKeys = enc_trial_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _enc_trial_key_allKeys = _enc_trial_key_allKeys.concat(theseKeys);
      if (_enc_trial_key_allKeys.length > 0) {
        enc_trial_key.keys = _enc_trial_key_allKeys[_enc_trial_key_allKeys.length - 1].name;  // just the last key pressed
        enc_trial_key.rt = _enc_trial_key_allKeys[_enc_trial_key_allKeys.length - 1].rt;
      }
    }
    
    
    // *enc_trial_text_block* updates
    if (t >= 0.0 && enc_trial_text_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_trial_text_block.tStart = t;  // (not accounting for frame time here)
      enc_trial_text_block.frameNStart = frameN;  // exact frame index
      
      enc_trial_text_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_trial_text_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_trial_text_block.setAutoDraw(false);
    }
    
    // *enc_trial_instructions_text* updates
    if (t >= 0.0 && enc_trial_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_trial_instructions_text.tStart = t;  // (not accounting for frame time here)
      enc_trial_instructions_text.frameNStart = frameN;  // exact frame index
      
      enc_trial_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_trial_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_trial_instructions_text.setAutoDraw(false);
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
    enc_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('enc_trial_key.keys', enc_trial_key.keys);
    if (typeof enc_trial_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_trial_key.rt', enc_trial_key.rt);
        }
    
    enc_trial_key.stop();
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
    response = enc_trial_key.keys;
    feedback_text = "";
    if ((response === "f")) {
        feedback_text = "Az \u00d6n v\u00e1lasza:\nA k\u00e9p nem marad.";
    } else {
        if ((response === "j")) {
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
    enc_practice_feedback_block.setText(block_name);
    // keep track of which components have finished
    enc_practice_feedbackComponents = [];
    enc_practice_feedbackComponents.push(enc_practice_feedback_interior);
    enc_practice_feedbackComponents.push(enc_practice_feedback_image);
    enc_practice_feedbackComponents.push(enc_practice_feedback_text);
    enc_practice_feedbackComponents.push(enc_practice_feedback_block);
    
    enc_practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    
    // *enc_practice_feedback_block* updates
    if (t >= 0.0 && enc_practice_feedback_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_practice_feedback_block.tStart = t;  // (not accounting for frame time here)
      enc_practice_feedback_block.frameNStart = frameN;  // exact frame index
      
      enc_practice_feedback_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_practice_feedback_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_practice_feedback_block.setAutoDraw(false);
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
    enc_practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    enc_practice_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _end_practice_key_allKeys;
var block_counter;
var end_practiceComponents;
function end_practiceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_practice'-------
    t = 0;
    end_practiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(600.000000);
    // update component parameters for each repeat
    end_practice_key.keys = undefined;
    end_practice_key.rt = undefined;
    _end_practice_key_allKeys = [];
    block_counter = 0;
    
    coming_up_next_text.setText(coming_up_text);
    // keep track of which components have finished
    end_practiceComponents = [];
    end_practiceComponents.push(end_practice_text);
    end_practiceComponents.push(end_practice_key);
    end_practiceComponents.push(end_practice_continue);
    end_practiceComponents.push(coming_up_next_text);
    
    end_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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

    frameRemains = 0.0 + 600.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 1.0 + 599.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_practice_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_practice_key.status = PsychoJS.Status.FINISHED;
  }

    if (end_practice_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_practice_key.getKeys({keyList: ['right', 'left'], waitRelease: false});
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

    frameRemains = 1.0 + 599.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_practice_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_practice_continue.setAutoDraw(false);
    }
    
    // *coming_up_next_text* updates
    if (t >= 0.0 && coming_up_next_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      coming_up_next_text.tStart = t;  // (not accounting for frame time here)
      coming_up_next_text.frameNStart = frameN;  // exact frame index
      
      coming_up_next_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 600.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (coming_up_next_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      coming_up_next_text.setAutoDraw(false);
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
    end_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    end_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_practice_key.keys', end_practice_key.keys);
    if (typeof end_practice_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_practice_key.rt', end_practice_key.rt);
        routineTimer.reset();
        }
    
    end_practice_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var recognition_titleComponents;
function recognition_titleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'recognition_title'-------
    t = 0;
    recognition_titleClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    recognition_titleComponents = [];
    recognition_titleComponents.push(start_recognition_text);
    
    recognition_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function recognition_titleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'recognition_title'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = recognition_titleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_recognition_text* updates
    if (t >= 0.0 && start_recognition_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_recognition_text.tStart = t;  // (not accounting for frame time here)
      start_recognition_text.frameNStart = frameN;  // exact frame index
      
      start_recognition_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_recognition_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_recognition_text.setAutoDraw(false);
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
    recognition_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recognition_titleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'recognition_title'-------
    recognition_titleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _rec_instructions_1_key_allKeys;
var rec_instructions_1Components;
function rec_instructions_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_instructions_1'-------
    t = 0;
    rec_instructions_1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    rec_instructions_1_key.keys = undefined;
    rec_instructions_1_key.rt = undefined;
    _rec_instructions_1_key_allKeys = [];
    // keep track of which components have finished
    rec_instructions_1Components = [];
    rec_instructions_1Components.push(rec_instructions_1_text);
    rec_instructions_1Components.push(rec_instructions_1_key);
    rec_instructions_1Components.push(rec_instructions_1_continue);
    
    rec_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_instructions_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_instructions_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_instructions_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_instructions_1_text* updates
    if (t >= 0.0 && rec_instructions_1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_1_text.tStart = t;  // (not accounting for frame time here)
      rec_instructions_1_text.frameNStart = frameN;  // exact frame index
      
      rec_instructions_1_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_1_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_1_text.setAutoDraw(false);
    }
    
    // *rec_instructions_1_key* updates
    if (t >= 5.0 && rec_instructions_1_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_1_key.tStart = t;  // (not accounting for frame time here)
      rec_instructions_1_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_instructions_1_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_1_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_1_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_1_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_1_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_instructions_1_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_instructions_1_key.getKeys({keyList: ['right'], waitRelease: false});
      _rec_instructions_1_key_allKeys = _rec_instructions_1_key_allKeys.concat(theseKeys);
      if (_rec_instructions_1_key_allKeys.length > 0) {
        rec_instructions_1_key.keys = _rec_instructions_1_key_allKeys[_rec_instructions_1_key_allKeys.length - 1].name;  // just the last key pressed
        rec_instructions_1_key.rt = _rec_instructions_1_key_allKeys[_rec_instructions_1_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rec_instructions_1_continue* updates
    if (t >= 5.0 && rec_instructions_1_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_1_continue.tStart = t;  // (not accounting for frame time here)
      rec_instructions_1_continue.frameNStart = frameN;  // exact frame index
      
      rec_instructions_1_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_1_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_1_continue.setAutoDraw(false);
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
    rec_instructions_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_instructions_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_instructions_1'-------
    rec_instructions_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_instructions_1_key.keys', rec_instructions_1_key.keys);
    if (typeof rec_instructions_1_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_instructions_1_key.rt', rec_instructions_1_key.rt);
        routineTimer.reset();
        }
    
    rec_instructions_1_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _rec_instructions_2_key_allKeys;
var rec_instructions_2Components;
function rec_instructions_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_instructions_2'-------
    t = 0;
    rec_instructions_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    rec_instructions_2_key.keys = undefined;
    rec_instructions_2_key.rt = undefined;
    _rec_instructions_2_key_allKeys = [];
    // keep track of which components have finished
    rec_instructions_2Components = [];
    rec_instructions_2Components.push(rec_instructions2_text);
    rec_instructions_2Components.push(rec_instructions_2_key);
    rec_instructions_2Components.push(rec_instructions_2_continue);
    rec_instructions_2Components.push(rec_instruction_2_title);
    
    rec_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_instructions_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_instructions_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_instructions_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_instructions2_text* updates
    if (t >= 0.0 && rec_instructions2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions2_text.tStart = t;  // (not accounting for frame time here)
      rec_instructions2_text.frameNStart = frameN;  // exact frame index
      
      rec_instructions2_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions2_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions2_text.setAutoDraw(false);
    }
    
    // *rec_instructions_2_key* updates
    if (t >= 5.0 && rec_instructions_2_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_2_key.tStart = t;  // (not accounting for frame time here)
      rec_instructions_2_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_instructions_2_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_2_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_2_key.clearEvents(); });
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_2_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_2_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_instructions_2_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_instructions_2_key.getKeys({keyList: ['right'], waitRelease: false});
      _rec_instructions_2_key_allKeys = _rec_instructions_2_key_allKeys.concat(theseKeys);
      if (_rec_instructions_2_key_allKeys.length > 0) {
        rec_instructions_2_key.keys = _rec_instructions_2_key_allKeys[_rec_instructions_2_key_allKeys.length - 1].name;  // just the last key pressed
        rec_instructions_2_key.rt = _rec_instructions_2_key_allKeys[_rec_instructions_2_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rec_instructions_2_continue* updates
    if (t >= 5.0 && rec_instructions_2_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_2_continue.tStart = t;  // (not accounting for frame time here)
      rec_instructions_2_continue.frameNStart = frameN;  // exact frame index
      
      rec_instructions_2_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_2_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_2_continue.setAutoDraw(false);
    }
    
    // *rec_instruction_2_title* updates
    if (t >= 0.0 && rec_instruction_2_title.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instruction_2_title.tStart = t;  // (not accounting for frame time here)
      rec_instruction_2_title.frameNStart = frameN;  // exact frame index
      
      rec_instruction_2_title.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instruction_2_title.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instruction_2_title.setAutoDraw(false);
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
    rec_instructions_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_instructions_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_instructions_2'-------
    rec_instructions_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_instructions_2_key.keys', rec_instructions_2_key.keys);
    if (typeof rec_instructions_2_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_instructions_2_key.rt', rec_instructions_2_key.rt);
        routineTimer.reset();
        }
    
    rec_instructions_2_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _rec_instructions_3_key_allKeys;
var rec_instructions_3Components;
function rec_instructions_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_instructions_3'-------
    t = 0;
    rec_instructions_3Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    rec_instructions_3_key.keys = undefined;
    rec_instructions_3_key.rt = undefined;
    _rec_instructions_3_key_allKeys = [];
    // keep track of which components have finished
    rec_instructions_3Components = [];
    rec_instructions_3Components.push(rec_instrauction_3_text);
    rec_instructions_3Components.push(rec_instructions_3_key);
    rec_instructions_3Components.push(rec_instructions_3_continue);
    rec_instructions_3Components.push(rec_instruction_3_title);
    
    rec_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_instructions_3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_instructions_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_instructions_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_instrauction_3_text* updates
    if (t >= 0.0 && rec_instrauction_3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instrauction_3_text.tStart = t;  // (not accounting for frame time here)
      rec_instrauction_3_text.frameNStart = frameN;  // exact frame index
      
      rec_instrauction_3_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instrauction_3_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instrauction_3_text.setAutoDraw(false);
    }
    
    // *rec_instructions_3_key* updates
    if (t >= 5 && rec_instructions_3_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_3_key.tStart = t;  // (not accounting for frame time here)
      rec_instructions_3_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_instructions_3_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_3_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_3_key.clearEvents(); });
    }

    frameRemains = 5 + 295 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_3_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_3_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_instructions_3_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_instructions_3_key.getKeys({keyList: ['right'], waitRelease: false});
      _rec_instructions_3_key_allKeys = _rec_instructions_3_key_allKeys.concat(theseKeys);
      if (_rec_instructions_3_key_allKeys.length > 0) {
        rec_instructions_3_key.keys = _rec_instructions_3_key_allKeys[_rec_instructions_3_key_allKeys.length - 1].name;  // just the last key pressed
        rec_instructions_3_key.rt = _rec_instructions_3_key_allKeys[_rec_instructions_3_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rec_instructions_3_continue* updates
    if (t >= 5.0 && rec_instructions_3_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_3_continue.tStart = t;  // (not accounting for frame time here)
      rec_instructions_3_continue.frameNStart = frameN;  // exact frame index
      
      rec_instructions_3_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 295.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_3_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_3_continue.setAutoDraw(false);
    }
    
    // *rec_instruction_3_title* updates
    if (t >= 0.0 && rec_instruction_3_title.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instruction_3_title.tStart = t;  // (not accounting for frame time here)
      rec_instruction_3_title.frameNStart = frameN;  // exact frame index
      
      rec_instruction_3_title.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instruction_3_title.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instruction_3_title.setAutoDraw(false);
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
    rec_instructions_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_instructions_3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_instructions_3'-------
    rec_instructions_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_instructions_3_key.keys', rec_instructions_3_key.keys);
    if (typeof rec_instructions_3_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_instructions_3_key.rt', rec_instructions_3_key.rt);
        routineTimer.reset();
        }
    
    rec_instructions_3_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _rec_instructions_4_key_allKeys;
var rec_instructions_4Components;
function rec_instructions_4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_instructions_4'-------
    t = 0;
    rec_instructions_4Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    rec_instructions_4_key.keys = undefined;
    rec_instructions_4_key.rt = undefined;
    _rec_instructions_4_key_allKeys = [];
    // keep track of which components have finished
    rec_instructions_4Components = [];
    rec_instructions_4Components.push(rec_instructions_4_text);
    rec_instructions_4Components.push(rec_instructions_4_key);
    rec_instructions_4Components.push(rec_instructions_4_continue);
    
    rec_instructions_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_instructions_4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_instructions_4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_instructions_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_instructions_4_text* updates
    if (t >= 0.0 && rec_instructions_4_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_4_text.tStart = t;  // (not accounting for frame time here)
      rec_instructions_4_text.frameNStart = frameN;  // exact frame index
      
      rec_instructions_4_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_4_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_4_text.setAutoDraw(false);
    }
    
    // *rec_instructions_4_key* updates
    if (t >= 1.0 && rec_instructions_4_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_4_key.tStart = t;  // (not accounting for frame time here)
      rec_instructions_4_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_instructions_4_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_4_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_instructions_4_key.clearEvents(); });
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_4_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_4_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_instructions_4_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_instructions_4_key.getKeys({keyList: ['right'], waitRelease: false});
      _rec_instructions_4_key_allKeys = _rec_instructions_4_key_allKeys.concat(theseKeys);
      if (_rec_instructions_4_key_allKeys.length > 0) {
        rec_instructions_4_key.keys = _rec_instructions_4_key_allKeys[_rec_instructions_4_key_allKeys.length - 1].name;  // just the last key pressed
        rec_instructions_4_key.rt = _rec_instructions_4_key_allKeys[_rec_instructions_4_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rec_instructions_4_continue* updates
    if (t >= 1.0 && rec_instructions_4_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_instructions_4_continue.tStart = t;  // (not accounting for frame time here)
      rec_instructions_4_continue.frameNStart = frameN;  // exact frame index
      
      rec_instructions_4_continue.setAutoDraw(true);
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_instructions_4_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_instructions_4_continue.setAutoDraw(false);
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
    rec_instructions_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_instructions_4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_instructions_4'-------
    rec_instructions_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_instructions_4_key.keys', rec_instructions_4_key.keys);
    if (typeof rec_instructions_4_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_instructions_4_key.rt', rec_instructions_4_key.rt);
        routineTimer.reset();
        }
    
    rec_instructions_4_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var demo_startComponents;
function demo_startRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'demo_start'-------
    t = 0;
    demo_startClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    demo_startComponents = [];
    demo_startComponents.push(demo_start_text);
    
    demo_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function demo_startRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'demo_start'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = demo_startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demo_start_text* updates
    if (t >= 0.0 && demo_start_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_start_text.tStart = t;  // (not accounting for frame time here)
      demo_start_text.frameNStart = frameN;  // exact frame index
      
      demo_start_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_start_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_start_text.setAutoDraw(false);
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
    demo_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demo_startRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'demo_start'-------
    demo_startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _demo_key_allKeys;
var demoComponents;
function demoRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'demo'-------
    t = 0;
    demoClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    demo_main_image.setPos([CurrentX, CurrentY]);
    demo_main_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    demo_main_image.setImage(CurrentImage);
    demo_image.setPos([DemoX, DemoY]);
    demo_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    demo_image.setImage(DemoImage);
    demo_text.setText(DemoText);
    demo_key.keys = undefined;
    demo_key.rt = undefined;
    _demo_key_allKeys = [];
    // keep track of which components have finished
    demoComponents = [];
    demoComponents.push(demo_interior);
    demoComponents.push(demo_main_image);
    demoComponents.push(demo_image);
    demoComponents.push(demo_text);
    demoComponents.push(demo_key);
    demoComponents.push(demo_continue);
    
    demoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function demoRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'demo'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = demoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demo_interior* updates
    if (t >= 0.0 && demo_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_interior.tStart = t;  // (not accounting for frame time here)
      demo_interior.frameNStart = frameN;  // exact frame index
      
      demo_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_interior.setAutoDraw(false);
    }
    
    // *demo_main_image* updates
    if (t >= 0.0 && demo_main_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_main_image.tStart = t;  // (not accounting for frame time here)
      demo_main_image.frameNStart = frameN;  // exact frame index
      
      demo_main_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_main_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_main_image.setAutoDraw(false);
    }
    
    // *demo_image* updates
    if (t >= 0.0 && demo_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_image.tStart = t;  // (not accounting for frame time here)
      demo_image.frameNStart = frameN;  // exact frame index
      
      demo_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_image.setAutoDraw(false);
    }
    
    // *demo_text* updates
    if (t >= 0.0 && demo_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_text.tStart = t;  // (not accounting for frame time here)
      demo_text.frameNStart = frameN;  // exact frame index
      
      demo_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_text.setAutoDraw(false);
    }
    
    // *demo_key* updates
    if (t >= 2.0 && demo_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_key.tStart = t;  // (not accounting for frame time here)
      demo_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demo_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demo_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demo_key.clearEvents(); });
    }

    frameRemains = 2.0 + 298 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_key.status = PsychoJS.Status.FINISHED;
  }

    if (demo_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = demo_key.getKeys({keyList: ['right'], waitRelease: false});
      _demo_key_allKeys = _demo_key_allKeys.concat(theseKeys);
      if (_demo_key_allKeys.length > 0) {
        demo_key.keys = _demo_key_allKeys[_demo_key_allKeys.length - 1].name;  // just the last key pressed
        demo_key.rt = _demo_key_allKeys[_demo_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *demo_continue* updates
    if (t >= 2.0 && demo_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_continue.tStart = t;  // (not accounting for frame time here)
      demo_continue.frameNStart = frameN;  // exact frame index
      
      demo_continue.setAutoDraw(true);
    }

    frameRemains = 2.0 + 298.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_continue.setAutoDraw(false);
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
    demoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demoRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'demo'-------
    demoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('demo_key.keys', demo_key.keys);
    if (typeof demo_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demo_key.rt', demo_key.rt);
        routineTimer.reset();
        }
    
    demo_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _demo_end_key_allKeys;
var demo_endComponents;
function demo_endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'demo_end'-------
    t = 0;
    demo_endClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    demo_end_key.keys = undefined;
    demo_end_key.rt = undefined;
    _demo_end_key_allKeys = [];
    // keep track of which components have finished
    demo_endComponents = [];
    demo_endComponents.push(demo_end_text);
    demo_endComponents.push(demo_end_key);
    demo_endComponents.push(demo_end_continue);
    
    demo_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function demo_endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'demo_end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = demo_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *demo_end_text* updates
    if (t >= 0.0 && demo_end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_end_text.tStart = t;  // (not accounting for frame time here)
      demo_end_text.frameNStart = frameN;  // exact frame index
      
      demo_end_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_end_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_end_text.setAutoDraw(false);
    }
    
    // *demo_end_key* updates
    if (t >= 1.0 && demo_end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_end_key.tStart = t;  // (not accounting for frame time here)
      demo_end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { demo_end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { demo_end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { demo_end_key.clearEvents(); });
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_end_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_end_key.status = PsychoJS.Status.FINISHED;
  }

    if (demo_end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = demo_end_key.getKeys({keyList: ['right'], waitRelease: false});
      _demo_end_key_allKeys = _demo_end_key_allKeys.concat(theseKeys);
      if (_demo_end_key_allKeys.length > 0) {
        demo_end_key.keys = _demo_end_key_allKeys[_demo_end_key_allKeys.length - 1].name;  // just the last key pressed
        demo_end_key.rt = _demo_end_key_allKeys[_demo_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *demo_end_continue* updates
    if (t >= 1.0 && demo_end_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      demo_end_continue.tStart = t;  // (not accounting for frame time here)
      demo_end_continue.frameNStart = frameN;  // exact frame index
      
      demo_end_continue.setAutoDraw(true);
    }

    frameRemains = 1.0 + 299.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (demo_end_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      demo_end_continue.setAutoDraw(false);
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
    demo_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function demo_endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'demo_end'-------
    demo_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('demo_end_key.keys', demo_end_key.keys);
    if (typeof demo_end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('demo_end_key.rt', demo_end_key.rt);
        routineTimer.reset();
        }
    
    demo_end_key.stop();
    coming_up_text = "Most a k\u00e9t feladatt\u00edpus egy\u00fcttes gyakorl\u00e1sa k\u00f6vetkezik.";
    
    return Scheduler.Event.NEXT;
  };
}


var _rec_fx_key_allKeys;
var rec_fxComponents;
function rec_fxRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_fx'-------
    t = 0;
    rec_fxClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    w_size = psychoJS.window.size;
    
    x_size = w_size[0];
    y_size = w_size[1];
    
    scr_resolution = (x_size / y_size);
    
    rec_fx_cross.setPos([CurrentX, CurrentY]);
    rec_fx_key.keys = undefined;
    rec_fx_key.rt = undefined;
    _rec_fx_key_allKeys = [];
    rec_fx_text_block.setText(block_name);
    // keep track of which components have finished
    rec_fxComponents = [];
    rec_fxComponents.push(rec_fx_interior);
    rec_fxComponents.push(rec_fx_cross);
    rec_fxComponents.push(rec_fx_key);
    rec_fxComponents.push(rec_fx_text_block);
    rec_fxComponents.push(rec_fx_instructions_text);
    
    rec_fxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_fxRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_fx'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_fxClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_fx_interior* updates
    if (t >= 0.0 && rec_fx_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_fx_interior.tStart = t;  // (not accounting for frame time here)
      rec_fx_interior.frameNStart = frameN;  // exact frame index
      
      rec_fx_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_fx_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_fx_interior.setAutoDraw(false);
    }
    
    // *rec_fx_cross* updates
    if (t >= 0.0 && rec_fx_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_fx_cross.tStart = t;  // (not accounting for frame time here)
      rec_fx_cross.frameNStart = frameN;  // exact frame index
      
      rec_fx_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_fx_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_fx_cross.setAutoDraw(false);
    }
    
    // *rec_fx_key* updates
    if (t >= 0.0 && rec_fx_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_fx_key.tStart = t;  // (not accounting for frame time here)
      rec_fx_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_fx_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_fx_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_fx_key.clearEvents(); });
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_fx_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_fx_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_fx_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_fx_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _rec_fx_key_allKeys = _rec_fx_key_allKeys.concat(theseKeys);
      if (_rec_fx_key_allKeys.length > 0) {
        rec_fx_key.keys = _rec_fx_key_allKeys[_rec_fx_key_allKeys.length - 1].name;  // just the last key pressed
        rec_fx_key.rt = _rec_fx_key_allKeys[_rec_fx_key_allKeys.length - 1].rt;
      }
    }
    
    
    // *rec_fx_text_block* updates
    if (t >= 0.0 && rec_fx_text_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_fx_text_block.tStart = t;  // (not accounting for frame time here)
      rec_fx_text_block.frameNStart = frameN;  // exact frame index
      
      rec_fx_text_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_fx_text_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_fx_text_block.setAutoDraw(false);
    }
    
    // *rec_fx_instructions_text* updates
    if (t >= 0.0 && rec_fx_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_fx_instructions_text.tStart = t;  // (not accounting for frame time here)
      rec_fx_instructions_text.frameNStart = frameN;  // exact frame index
      
      rec_fx_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Jitter / 1000) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_fx_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_fx_instructions_text.setAutoDraw(false);
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
    rec_fxComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_fxRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_fx'-------
    rec_fxComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_fx_key.keys', rec_fx_key.keys);
    if (typeof rec_fx_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_fx_key.rt', rec_fx_key.rt);
        }
    
    rec_fx_key.stop();
    // the Routine "rec_fx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _rec_trial_key_allKeys;
var rec_trialComponents;
function rec_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_trial'-------
    t = 0;
    rec_trialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    rec_trial_main_image.setPos([CurrentX, CurrentY]);
    rec_trial_main_image.setSize([0.3125, (0.3125 * scr_resolution)]);
    rec_trial_main_image.setImage(CurrentImage);
    rec_trial_key.keys = undefined;
    rec_trial_key.rt = undefined;
    _rec_trial_key_allKeys = [];
    rec_trial_text_block.setText(block_name);
    // keep track of which components have finished
    rec_trialComponents = [];
    rec_trialComponents.push(rec_trial_interior);
    rec_trialComponents.push(rec_trial_main_image);
    rec_trialComponents.push(rec_trial_key);
    rec_trialComponents.push(rec_trial_text_block);
    rec_trialComponents.push(rec_trial_instructions_text);
    
    rec_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_trial_interior* updates
    if (t >= 0.0 && rec_trial_interior.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_trial_interior.tStart = t;  // (not accounting for frame time here)
      rec_trial_interior.frameNStart = frameN;  // exact frame index
      
      rec_trial_interior.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_trial_interior.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_trial_interior.setAutoDraw(false);
    }
    
    // *rec_trial_main_image* updates
    if (t >= 0.0 && rec_trial_main_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_trial_main_image.tStart = t;  // (not accounting for frame time here)
      rec_trial_main_image.frameNStart = frameN;  // exact frame index
      
      rec_trial_main_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_trial_main_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_trial_main_image.setAutoDraw(false);
    }
    
    // *rec_trial_key* updates
    if (t >= 0.0 && rec_trial_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_trial_key.tStart = t;  // (not accounting for frame time here)
      rec_trial_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rec_trial_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rec_trial_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rec_trial_key.clearEvents(); });
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_trial_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_trial_key.status = PsychoJS.Status.FINISHED;
  }

    if (rec_trial_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rec_trial_key.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _rec_trial_key_allKeys = _rec_trial_key_allKeys.concat(theseKeys);
      if (_rec_trial_key_allKeys.length > 0) {
        rec_trial_key.keys = _rec_trial_key_allKeys[_rec_trial_key_allKeys.length - 1].name;  // just the last key pressed
        rec_trial_key.rt = _rec_trial_key_allKeys[_rec_trial_key_allKeys.length - 1].rt;
      }
    }
    
    
    // *rec_trial_text_block* updates
    if (t >= 0.0 && rec_trial_text_block.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_trial_text_block.tStart = t;  // (not accounting for frame time here)
      rec_trial_text_block.frameNStart = frameN;  // exact frame index
      
      rec_trial_text_block.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_trial_text_block.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_trial_text_block.setAutoDraw(false);
    }
    
    // *rec_trial_instructions_text* updates
    if (t >= 0.0 && rec_trial_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_trial_instructions_text.tStart = t;  // (not accounting for frame time here)
      rec_trial_instructions_text.frameNStart = frameN;  // exact frame index
      
      rec_trial_instructions_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_trial_instructions_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_trial_instructions_text.setAutoDraw(false);
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
    rec_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_trial'-------
    rec_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('rec_trial_key.keys', rec_trial_key.keys);
    if (typeof rec_trial_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rec_trial_key.rt', rec_trial_key.rt);
        }
    
    rec_trial_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var correct_response;
var rec_practice_feedbackComponents;
function rec_practice_feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'rec_practice_feedback'-------
    t = 0;
    rec_practice_feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    correct_response = "";
    if ((StimType === "FOIL")) {
        correct_response = "A helyes v\u00e1lasz: \u00daj";
    } else {
        if ((StimType === "LURE")) {
            correct_response = "A helyes v\u00e1lasz: \u00daj";
        } else {
            if ((StimType === "TARGET")) {
                correct_response = "A helyes v\u00e1lasz: R\u00e9gi";
            }
        }
    }
    response = "";
    if ((rec_trial_key.keys === "f")) {
        response = "Az \u00d6n v\u00e1lasza: R\u00e9gi";
    } else {
        if ((rec_trial_key.keys === "j")) {
            response = "Az \u00d6n v\u00e1lasza: \u00daj";
        }
    }
    feedback_text = ((correct_response + "\n") + response);
    
    rec_practice_feedback_text.setText(feedback_text);
    // keep track of which components have finished
    rec_practice_feedbackComponents = [];
    rec_practice_feedbackComponents.push(rec_practice_feedback_text);
    
    rec_practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function rec_practice_feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'rec_practice_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = rec_practice_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rec_practice_feedback_text* updates
    if (t >= 0.0 && rec_practice_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_practice_feedback_text.tStart = t;  // (not accounting for frame time here)
      rec_practice_feedback_text.frameNStart = frameN;  // exact frame index
      
      rec_practice_feedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rec_practice_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rec_practice_feedback_text.setAutoDraw(false);
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
    rec_practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function rec_practice_feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'rec_practice_feedback'-------
    rec_practice_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var block_titleComponents;
function block_titleRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'block_title'-------
    t = 0;
    block_titleClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    block_title_text.setText(block_name);
    // keep track of which components have finished
    block_titleComponents = [];
    block_titleComponents.push(block_title_text);
    
    block_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function block_titleRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'block_title'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = block_titleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *block_title_text* updates
    if (t >= 0.0 && block_title_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block_title_text.tStart = t;  // (not accounting for frame time here)
      block_title_text.frameNStart = frameN;  // exact frame index
      
      block_title_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (block_title_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      block_title_text.setAutoDraw(false);
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
    block_titleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function block_titleRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'block_title'-------
    block_titleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    coming_up_text = "A feladat k\u00f6vetkezik. A feladat sor\u00e1n m\u00e1r nem kap visszajelz\u00e9st.";
    
    return Scheduler.Event.NEXT;
  };
}


var end_run_text;
var start_runComponents;
function start_runRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'start_run'-------
    t = 0;
    start_runClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    run_counter = (run_counter + 1);
    end_run_text = "R\u00f6vid sz\u00fcnet.\n\nA feladat folytat\u00e1shoz nyomja le a jobb nyilat.";
    if ((run_counter === 3)) {
        end_run_text = "V\u00e9ge a feladat els\u0151 fel\u00e9nek. A folytat\u00e1shoz nyomja le a jobb nyilat.";
    } else {
        if ((run_counter === 6)) {
            end_run_text = "V\u00e9ge a feladatnak. A folytat\u00e1shoz nyomja le a jobb nyilat.";
        }
    }
    
    // keep track of which components have finished
    start_runComponents = [];
    start_runComponents.push(start_enc_run_text);
    
    start_runComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function start_runRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'start_run'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = start_runClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_enc_run_text* updates
    if (t >= 0.0 && start_enc_run_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_enc_run_text.tStart = t;  // (not accounting for frame time here)
      start_enc_run_text.frameNStart = frameN;  // exact frame index
      
      start_enc_run_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    start_runComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_runRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'start_run'-------
    start_runComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var rec_start;
var rec_selection;
var enc_start;
var enc_selection;
var init_blocksComponents;
function init_blocksRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'init_blocks'-------
    t = 0;
    init_blocksClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    block_name = "";
    if ((TrialType === "OBJ")) {
        block_name = "K\u00e9p";
    } else {
        if ((TrialType === "LOC")) {
            block_name = "Hely";
        } else {
            block_name = "Block Unknown";
        }
    }
    
    rec_start = rec_end;
    rec_end = (rec_start + 24);
    rec_selection = Array.from({length: rec_end - rec_start}, (_, index) => index + rec_start)
    
    
    
    start_rec_block_text.setText(block_name);
    enc_start = enc_end;
    enc_end = (enc_start + 50);
    enc_selection = Array.from({length: enc_end - enc_start}, (_, index) => index + enc_start);
    
    // keep track of which components have finished
    init_blocksComponents = [];
    init_blocksComponents.push(start_rec_block_text);
    
    init_blocksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function init_blocksRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'init_blocks'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = init_blocksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_rec_block_text* updates
    if (t >= 0.0 && start_rec_block_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_rec_block_text.tStart = t;  // (not accounting for frame time here)
      start_rec_block_text.frameNStart = frameN;  // exact frame index
      
      start_rec_block_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_rec_block_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      start_rec_block_text.setAutoDraw(false);
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
    init_blocksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function init_blocksRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'init_blocks'-------
    init_blocksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _enc_run_end_key_allKeys;
var end_runComponents;
function end_runRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_run'-------
    t = 0;
    end_runClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1201.000000);
    // update component parameters for each repeat
    end_enc_run_text.setText(end_run_text);
    enc_run_end_key.keys = undefined;
    enc_run_end_key.rt = undefined;
    _enc_run_end_key_allKeys = [];
    // keep track of which components have finished
    end_runComponents = [];
    end_runComponents.push(end_enc_run_text);
    end_runComponents.push(enc_run_end_key);
    
    end_runComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function end_runRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_run'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_runClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_enc_run_text* updates
    if (t >= 0.0 && end_enc_run_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_enc_run_text.tStart = t;  // (not accounting for frame time here)
      end_enc_run_text.frameNStart = frameN;  // exact frame index
      
      end_enc_run_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1200 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_enc_run_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_enc_run_text.setAutoDraw(false);
    }
    
    // *enc_run_end_key* updates
    if (t >= 1.0 && enc_run_end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enc_run_end_key.tStart = t;  // (not accounting for frame time here)
      enc_run_end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enc_run_end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enc_run_end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enc_run_end_key.clearEvents(); });
    }

    frameRemains = 1.0 + 1200 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (enc_run_end_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      enc_run_end_key.status = PsychoJS.Status.FINISHED;
  }

    if (enc_run_end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = enc_run_end_key.getKeys({keyList: ['right'], waitRelease: false});
      _enc_run_end_key_allKeys = _enc_run_end_key_allKeys.concat(theseKeys);
      if (_enc_run_end_key_allKeys.length > 0) {
        enc_run_end_key.keys = _enc_run_end_key_allKeys[_enc_run_end_key_allKeys.length - 1].name;  // just the last key pressed
        enc_run_end_key.rt = _enc_run_end_key_allKeys[_enc_run_end_key_allKeys.length - 1].rt;
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
    end_runComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_runRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_run'-------
    end_runComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('enc_run_end_key.keys', enc_run_end_key.keys);
    if (typeof enc_run_end_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enc_run_end_key.rt', enc_run_end_key.rt);
        routineTimer.reset();
        }
    
    enc_run_end_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var end_task_text;
var _inter_task_break_key_allKeys;
var inter_task_breakComponents;
function inter_task_breakRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'inter_task_break'-------
    t = 0;
    inter_task_breakClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1200.000000);
    // update component parameters for each repeat
    block_name_selection = [151, 201, 251];
    end_task_text = "Miel\u0151tt tov\u00e1bb l\u00e9pne a k\u00f6vetkez\u0151 feladathoz, tartson egy r\u00f6vid sz\u00fcnetet, hogy felfriss\u00fclj\u00f6n. Ha teheti, \u00e1lljon fel a sz\u00e1m\u00edt\u00f3g\u00e9pt\u0151l, pihentesse szemeit, igyon egy poh\u00e1r vizet. \u00dcgyeljen, hogy ez a sz\u00fcnet ne tartson 10 percn\u00e9l tov\u00e1bb. ";
    if ((run_counter >= 6)) {
        end_task_text = "Feltesz\u00fcnk \u00d6nnek p\u00e1r k\u00e9rd\u00e9st, majd megkapja a vizsg\u00e1lat elv\u00e9gz\u00e9s\u00e9t igazol\u00f3 k\u00f3dot.";
    }
    
    inter_task_break_text.setText(end_task_text);
    inter_task_break_key.keys = undefined;
    inter_task_break_key.rt = undefined;
    _inter_task_break_key_allKeys = [];
    // keep track of which components have finished
    inter_task_breakComponents = [];
    inter_task_breakComponents.push(inter_task_break_continue);
    inter_task_breakComponents.push(inter_task_break_text);
    inter_task_breakComponents.push(inter_task_break_key);
    
    inter_task_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    
    // *inter_task_break_continue* updates
    if (t >= 5.0 && inter_task_break_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inter_task_break_continue.tStart = t;  // (not accounting for frame time here)
      inter_task_break_continue.frameNStart = frameN;  // exact frame index
      
      inter_task_break_continue.setAutoDraw(true);
    }

    frameRemains = 5.0 + 1195.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (inter_task_break_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      inter_task_break_continue.setAutoDraw(false);
    }
    
    // *inter_task_break_text* updates
    if (t >= 0.0 && inter_task_break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inter_task_break_text.tStart = t;  // (not accounting for frame time here)
      inter_task_break_text.frameNStart = frameN;  // exact frame index
      
      inter_task_break_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1200.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (inter_task_break_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      inter_task_break_text.setAutoDraw(false);
    }
    
    // *inter_task_break_key* updates
    if (t >= 5.0 && inter_task_break_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inter_task_break_key.tStart = t;  // (not accounting for frame time here)
      inter_task_break_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { inter_task_break_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { inter_task_break_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { inter_task_break_key.clearEvents(); });
    }

    frameRemains = 5.0 + 1195 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (inter_task_break_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      inter_task_break_key.status = PsychoJS.Status.FINISHED;
  }

    if (inter_task_break_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = inter_task_break_key.getKeys({keyList: ['right'], waitRelease: false});
      _inter_task_break_key_allKeys = _inter_task_break_key_allKeys.concat(theseKeys);
      if (_inter_task_break_key_allKeys.length > 0) {
        inter_task_break_key.keys = _inter_task_break_key_allKeys[_inter_task_break_key_allKeys.length - 1].name;  // just the last key pressed
        inter_task_break_key.rt = _inter_task_break_key_allKeys[_inter_task_break_key_allKeys.length - 1].rt;
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
    inter_task_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    inter_task_breakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('inter_task_break_key.keys', inter_task_break_key.keys);
    if (typeof inter_task_break_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('inter_task_break_key.rt', inter_task_break_key.rt);
        routineTimer.reset();
        }
    
    inter_task_break_key.stop();
    return Scheduler.Event.NEXT;
  };
}


var _end_experiment_key_allKeys;
var end_experimentComponents;
function end_experimentRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_experiment'-------
    t = 0;
    end_experimentClock.reset(); // clock
    frameN = -1;
    routineTimer.add(300.000000);
    // update component parameters for each repeat
    
    
    end_experiment_code.setText(code);
    end_experiment_key.keys = undefined;
    end_experiment_key.rt = undefined;
    _end_experiment_key_allKeys = [];
    // keep track of which components have finished
    end_experimentComponents = [];
    end_experimentComponents.push(end_experiment_text);
    end_experimentComponents.push(end_experiment_code);
    end_experimentComponents.push(end_experiment_continue);
    end_experimentComponents.push(end_experiment_key);
    
    end_experimentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function end_experimentRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_experiment'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_experimentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_experiment_text* updates
    if (t >= 0.0 && end_experiment_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_experiment_text.tStart = t;  // (not accounting for frame time here)
      end_experiment_text.frameNStart = frameN;  // exact frame index
      
      end_experiment_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_experiment_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_experiment_text.setAutoDraw(false);
    }
    
    // *end_experiment_code* updates
    if (t >= 0.0 && end_experiment_code.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_experiment_code.tStart = t;  // (not accounting for frame time here)
      end_experiment_code.frameNStart = frameN;  // exact frame index
      
      end_experiment_code.setAutoDraw(true);
    }

    frameRemains = 0.0 + 300.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_experiment_code.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_experiment_code.setAutoDraw(false);
    }
    
    // *end_experiment_continue* updates
    if (t >= 3.0 && end_experiment_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_experiment_continue.tStart = t;  // (not accounting for frame time here)
      end_experiment_continue.frameNStart = frameN;  // exact frame index
      
      end_experiment_continue.setAutoDraw(true);
    }

    frameRemains = 3.0 + 297.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_experiment_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_experiment_continue.setAutoDraw(false);
    }
    
    // *end_experiment_key* updates
    if (t >= 4.0 && end_experiment_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_experiment_key.tStart = t;  // (not accounting for frame time here)
      end_experiment_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_experiment_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_experiment_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_experiment_key.clearEvents(); });
    }

    frameRemains = 4.0 + 294.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_experiment_key.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_experiment_key.status = PsychoJS.Status.FINISHED;
  }

    if (end_experiment_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_experiment_key.getKeys({keyList: ['right'], waitRelease: false});
      _end_experiment_key_allKeys = _end_experiment_key_allKeys.concat(theseKeys);
      if (_end_experiment_key_allKeys.length > 0) {
        end_experiment_key.keys = _end_experiment_key_allKeys[_end_experiment_key_allKeys.length - 1].name;  // just the last key pressed
        end_experiment_key.rt = _end_experiment_key_allKeys[_end_experiment_key_allKeys.length - 1].rt;
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
    end_experimentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_experimentRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_experiment'-------
    end_experimentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end_experiment_key.keys', end_experiment_key.keys);
    if (typeof end_experiment_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_experiment_key.rt', end_experiment_key.rt);
        routineTimer.reset();
        }
    
    end_experiment_key.stop();
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
