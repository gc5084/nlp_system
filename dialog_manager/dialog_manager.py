from datetime import date, timedelta

from data import dialog_data
from semantic import semantic_analysis
from state_manager.state_manager import *
from syntactic import syntactic_analysis

TICKERS_WORDS = ['bitcoin', 'euro', 'ripple', 'iota']
SEARCH_VERBS = ['give', 'show', 'get', 'list', 'display', 'search', 'retrieve', 'find']
OPERATION_WORDS = ['price', 'volume', 'low', 'high']
NOT_CURRENT_WORDS = ['yesterday', 'last week', 'last month', 'last year']
START_CONVERSATION = "What is your name ?"
DATE_MAPPERS = {
    'yesterday': date.today() - timedelta(days=1),
    'last week': date.today() - timedelta(weeks=1),
    'last month': date.today() - timedelta(weeks=4),
    'last year': date.today() - timedelta(days=365)
}


class DialogManager:
    def __init__(self):
        self.state = INITIAL_STATE
        self.context = dialog_data.DialogContext()
        self.syntactic_analyzer = syntactic_analysis.SyntaticAnalyzer()
        self.semantic_analyzer = semantic_analysis.SemanticAnalyzer()

    def process_input(self, text):
        analyzed_text = self.syntactic_analyzer.analyze(text)
        if self.state == INITIAL_STATE:
            self.context.ticker, self.context.operation, self.context.date = self.parse_search(text, analyzed_text)

        state_manager = StateManager(self.get_state())
        state_manager.move_forward(self.context)

    def get_state(self):
        return self.state

    def parse_search(self, text, analyzed_text):
        root = next((x for x in analyzed_text if x['dep'] == 'ROOT'), None)
        operation = next((x for x in root['children'] if x.lemma_ in OPERATION_WORDS), None)
        ticker = next((x['lemma'] for x in analyzed_text if x['pos'] == 'NOUN' and x['lemma'] in TICKERS_WORDS), None)
        date = next((x['lemma'] for x in analyzed_text if x['pos'] == 'NOUN' and x['lemma'] in NOT_CURRENT_WORDS), None)
        print("Operation " + operation.lemma_)
        print("Ticker " + ticker)
#        print("Date " + date)
        return ticker, operation.lemma_, date
