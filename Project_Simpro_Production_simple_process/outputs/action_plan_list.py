
import outputs.process_actions.process_variant_0 as pv_0

import outputs.process_actions.process_variant_1 as pv_1

import outputs.process_actions.process_variant_2 as pv_2

import outputs.process_actions.process_variant_3 as pv_3

import outputs.process_actions.process_variant_4 as pv_4

import outputs.process_actions.process_variant_5 as pv_5



class action_plan_definer():
   
   def __init__(self):
        self.action_plan_list = []

action_plan_definer_instance = action_plan_definer()



action_plan_definer_instance.action_plan_list.append(pv_0.action_plan)

action_plan_definer_instance.action_plan_list.append(pv_1.action_plan)

action_plan_definer_instance.action_plan_list.append(pv_2.action_plan)

action_plan_definer_instance.action_plan_list.append(pv_3.action_plan)

action_plan_definer_instance.action_plan_list.append(pv_4.action_plan)

action_plan_definer_instance.action_plan_list.append(pv_5.action_plan)
