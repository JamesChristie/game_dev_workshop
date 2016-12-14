import unittest

from engine.game_step import GameStep

def step_one(game_state):
  game_state['test_key'] = '1'

def step_two(game_state):
  if game_state.get('test_key'):
    game_state['test_key'] += '2'

class TestGameStep(unittest.TestCase):
  def setUp(self):
    self.game_step = GameStep()

  def test_add_procedure(self):
    self.game_step.add_procedure(step_one)
    steps = self.game_step.get_procedures()

    self.assertEqual(steps, [step_one])

    self.game_step.add_procedure(step_two)
    steps = self.game_step.get_procedures()

    self.assertEqual(steps, [step_one, step_two])

  def test_remove_procedure(self):
    self.game_step.add_procedure(step_one)
    self.game_step.add_procedure(step_two)
    self.game_step.remove_procedure(step_one)
    steps = self.game_step.get_procedures()

    self.assertEqual(steps, [step_two])

  def test_execution(self):
    game_state = {}

    self.game_step.add_procedure(step_one)
    self.game_step.add_procedure(step_two)
    self.game_step.execute(game_state)

    self.assertEqual('12', game_state.get('test_key'))

  def test_execution_order(self):
    game_state = {}

    # Opposite order of previous test
    self.game_step.add_procedure(step_two)
    self.game_step.add_procedure(step_one)
    self.game_step.execute(game_state)

    self.assertEqual('1', game_state.get('test_key'))
