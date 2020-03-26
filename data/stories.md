## story1_11_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_1  
  - utter_q1_one_apo1
  - utter_q1_one_apo2           
  - utter_q1_one_a
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story1_11_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_1  
  - utter_q1_one_apo1
  - utter_q1_one_apo2           
  - utter_q1_one_a
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story1_00 _confirm         
* greet     
  - utter_greet
  - utter_q1
* mood_1 
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story1_00_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_1 
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story1_01_confirm
* greet     
  - utter_greet
  - utter_q1
* mood_1  
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story1_01_deny
* greet     
  - utter_greet
  - utter_q1
* mood_1  
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
 - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story1_10_confirm
* greet     
  - utter_greet
  - utter_q1
* mood_1 
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story1_10_deny
* greet     
  - utter_greet
  - utter_q1
* mood_1 
  - utter_q1_one_apo1
  - utter_q1_one_apo2 
  - utter_q1_one_a
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_111_confirm         
* greet     
  - utter_greet
  - utter_q1
* mood_2
  - utter_q1_two_apo1
  - utter_q1_two_apo2             
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_111_deny          
* greet     
  - utter_greet
  - utter_q1
* mood_2
  - utter_q1_two_apo1
  - utter_q1_two_apo2             
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story2_000_confirm          
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null} 
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_000_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null} 
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_001_confirm         
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null} 
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_001_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null} 
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_010_confirm         
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_010_deny          
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story2_011_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_011_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_100_confirm          
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_100_deny          
* greet     
  - utter_greet
  - utter_q1
* mood_2  
  - utter_q1_two_apo1
  - utter_q1_two_apo2           
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_101_confirm           
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_101_deny           
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1
  - utter_q1_two_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_110_confirm           
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1
  - feedback_form3
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story2_110_deny           
* greet     
  - utter_greet
  - utter_q1
* mood_2 
  - utter_q1_two_apo1
  - utter_q1_two_apo2            
  - utter_q1_two_a
* options_q1
  - feedback_form3
  - utter_q1_two_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_111_confirm           
* greet     
  - utter_greet
  - utter_q1
* mood_3  
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_111_deny            
* greet     
  - utter_greet
  - utter_q1
* mood_3  
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7




## story3_000_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story3_000_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_001_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_3  
  - utter_q1_three_apo1
  - utter_q1_three_apo2           
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_001_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_3  
  - utter_q1_three_apo1
  - utter_q1_three_apo2           
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_010_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_010_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_011_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_011_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story3_100_confirm      
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story3_100_deny      
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_101_confirm  
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story3_101_deny   
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story3_110_confirm        
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story3_110_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_3 
  - utter_q1_three_apo1
  - utter_q1_three_apo2            
  - utter_q1_three_a
* options_q1
  - utter_q1_three_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_111_confirm          
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_111_deny         
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story4_000_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4
  - utter_q1_four_apo1
  - utter_q1_four_apo2             
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story4_000_deny      
* greet     
  - utter_greet
  - utter_q1
* mood_4
  - utter_q1_four_apo1
  - utter_q1_four_apo2             
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_001_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4
  - utter_q1_four_apo1
  - utter_q1_four_apo2             
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_001_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_4
  - utter_q1_four_apo1
  - utter_q1_four_apo2             
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_010_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_010_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_010_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_010_deny      
* greet     
  - utter_greet
  - utter_q1
* mood_4 
  - utter_q1_four_apo1
  - utter_q1_four_apo2            
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_011_confirm      
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_011_deny      
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_100_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_100_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_101_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_4   
  - utter_q1_four_apo1
  - utter_q1_four_apo2          
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_101_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_4   
  - utter_q1_four_apo1
  - utter_q1_four_apo2          
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_110_confirm      
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story4_110_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_4  
  - utter_q1_four_apo1
  - utter_q1_four_apo2           
  - utter_q1_four_a
* options_q1
  - utter_q1_four_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story5_111_confirm       
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_000_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_001_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_010_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_011_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story5_100_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_101_confirm            
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_110_confirm           
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* confirm
  - feedback_form
  - form{"name": "feedback_form"}
  - form{"name": null}
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story5_111_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_000_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_001_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_010_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_011_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1{"opt":"Others"}
  - feedback_form3
  - form{"name": "feedback_form3"}
  - form{"name": null}
  - utter_q1_five_b
* options_q1
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7


## story5_100_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_101_deny        
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{"opt2":"Extra Input"}
  - feedback_form4
  - form{"name": "feedback_form4"}
  - form{"name": null}
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7

## story5_110_deny       
* greet     
  - utter_greet
  - utter_q1
* mood_5 
  - utter_q1_five_apo1            
  - utter_q1_five_a
* options_q1
  - utter_q1_five_b
* options_q1{
  - utter_q2
* user_options
  - action_mood_identifier
* options_q2{"opt1":"Additional Input"}
  - feedback_form5
  - form{"name": "feedback_form5"}
  - form{"name": null}
  - utter_question
* deny
  - feedback_form1
  - form{"name": "feedback_form1"}
  - form{"name": null}
  - utter_q6
* mood_happy OR mood_unhappy
  - action_mood_identifier6
* mood_happy OR mood_unhappy
  - action_mood_identifier7







