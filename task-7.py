state = {
    "monkey": "door",
    "box": "window",
    "on_box": False,
    "has_banana": False
}

goal_stack = ["HAS_BANANA"]

while goal_stack:
    goal = goal_stack.pop()

    if goal == "HAS_BANANA":
        if not state["has_banana"]:
            goal_stack += [
                "GRASP_BANANA",
                "MONKEY_UNDER_BANANA",
                "ON_BOX",
                "BOX_UNDER_BANANA"
            ]

    elif goal == "BOX_UNDER_BANANA":
        state["box"] = "ceiling"
        print("Move box under the banana")

    elif goal == "ON_BOX":
        state["monkey"] = state["box"]
        state["on_box"] = True
        print("Monkey moves to the box and climbs onto it")

    elif goal == "MONKEY_UNDER_BANANA":
        state["monkey"] = "ceiling"
        print("Monkey moves under the banana")

    elif goal == "GRASP_BANANA":
        if state["on_box"] and state["monkey"] == "ceiling":
            state["has_banana"] = True
            print("Monkey grasps the banana")

print("\nGoal Achieved:", state["has_banana"])
