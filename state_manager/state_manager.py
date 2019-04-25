
INITIAL_STATE = "INITIAL_STATE"
SHOW_PRICE_ASK_OTHERS = "SHOW_PRICE_ASK_OTHERS"
SHOW_PRICE_DATED_ASK_OTHERS = "SHOW_PRICE_DATED_ASK_OTHERS"
SHOW_VOLUME_ASK_OTHERS = "SHOW_VOLUME_ASK_OTHERS"
SHOW_VOLUME_DATED_ASK_OTHERS = "SHOW_VOLUME_DATED_ASK_OTHERS"
SHOW_HIGH_ASK_OTHERS = "SHOW_HIGH_ASK_OTHERS"
SHOW_HIGH_DATED_ASK_OTHERS = "SHOW_HIGH_DATED_ASK_OTHERS"
SHOW_LOW_ASK_OTHERS = "SHOW_LOW_ASK_OTHERS"
SHOW_LOW_DATED_ASK_OTHERS = "SHOW_LOW_DATED_ASK_OTHERS"
ANY_OTHER_REQUEST = "ANY_OTHER_REQUEST"
HAVE_A_GOOD_DAY = "HAVE_A_GOOD_DAY"


class State:
	def __init__(self, value, readiness_function):
		self.readiness_function = readiness_function
		self.value = value

	def can_move(self, dialogue_context):
		return self.readiness_function(dialogue_context)


def to_price_dated(dialogue_context):
	return dialogue_context.operation == "price" and dialogue_context.ticker is not None \
	       and dialogue_context.date is not None


def to_volume_dated(dialogue_context):
	return dialogue_context.operation == "volume" and dialogue_context.ticker is not None \
	       and dialogue_context.date is not None


def to_high_dated(dialogue_context):
	return dialogue_context.operation == "high" and dialogue_context.ticker is not None \
	       and dialogue_context.date is not None


def to_low_dated(dialogue_context):
	return dialogue_context.operation == "low" and dialogue_context.ticker is not None \
	       and dialogue_context.date is not None

def to_price(dialogue_context):
	return dialogue_context.operation == "price" and dialogue_context.ticker is not None \
	       and dialogue_context.date is None

def to_volume(dialogue_context):
	return dialogue_context.operation == "volume" and dialogue_context.ticker is not None \
	       and dialogue_context.date is None

def to_high(dialogue_context):
	return dialogue_context.operation == "high" and dialogue_context.ticker is not None \
	       and dialogue_context.date is None

def to_low(dialogue_context):
	return dialogue_context.operation == "low" and dialogue_context.ticker is not None \
	       and dialogue_context.date is None


class StateManager:
	def __init__(self, current_state=None):
		self.current_state = current_state

	def move_forward(self, dialog_context):
		children_states = STATE_AUTOMATON[self.current_state]
		print("Children states " + str(children_states))
		for child_state in children_states:
			if child_state.can_move(dialog_context):
				print("I can move to " + child_state.value)
				self.current_state = child_state
				break



STATE_AUTOMATON = {
	INITIAL_STATE: [ # What is your request ?
					State(SHOW_PRICE_ASK_OTHERS, to_price),
					State(SHOW_PRICE_DATED_ASK_OTHERS, to_price_dated),
	                State(SHOW_VOLUME_ASK_OTHERS, to_volume),
					State(SHOW_VOLUME_DATED_ASK_OTHERS, to_volume_dated),
	                State(SHOW_HIGH_ASK_OTHERS, to_high),
					State(SHOW_HIGH_DATED_ASK_OTHERS, to_high_dated),
	                State(SHOW_LOW_ASK_OTHERS, to_low),
					State(SHOW_LOW_DATED_ASK_OTHERS, to_low_dated)
	                ],
	SHOW_PRICE_ASK_OTHERS: [ # Would you like to know other value for the ticker given ?
	                State(SHOW_VOLUME_ASK_OTHERS, to_volume),
					State(SHOW_VOLUME_DATED_ASK_OTHERS, to_volume_dated),
	                State(SHOW_HIGH_ASK_OTHERS, to_high),
					State(SHOW_HIGH_DATED_ASK_OTHERS, to_high_dated),
	                State(SHOW_LOW_ASK_OTHERS, to_low),
					State(SHOW_LOW_DATED_ASK_OTHERS, to_low_dated)
	                        ],
	SHOW_VOLUME_ASK_OTHERS: [ # Would you like to know other value for the ticker given ?
	                State(SHOW_PRICE_ASK_OTHERS, to_price),
					State(SHOW_PRICE_DATED_ASK_OTHERS, to_price_dated),
	                State(SHOW_HIGH_ASK_OTHERS, to_high),
					State(SHOW_HIGH_DATED_ASK_OTHERS, to_high_dated),
	                State(SHOW_LOW_ASK_OTHERS, to_low),
					State(SHOW_LOW_DATED_ASK_OTHERS, to_low_dated)
	                        ],
	ANY_OTHER_REQUEST: [HAVE_A_GOOD_DAY]
}