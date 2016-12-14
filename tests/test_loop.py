import unittest

from engine import loop

# NOTE (jchristie@8thlight.com) Python doesn't allow access
# to module-scoped variables by default, so functions/classes
# wanting to access them must declare them as 'global' in any
# scope that they make use of them. Otherwise, the variable
# will be undeclared in that scope.
run_count = 0
game_state = {}

def run_twice_guard(game_state):
  global run_count
  return run_count >= 2

def incrementor_procedure(game_state):
  global run_count
  run_count += 1

def game_state_guard(game_state):
  return (game_state.get('run_count') and
    game_state['run_count'] >= 3)

def game_state_mutator_procedure(game_state):
  if not game_state.get('run_count'):
    game_state['run_count'] = 0

  game_state['run_count'] += 1

class TestLoop(unittest.TestCase):
  def setUp(self):
    global run_count
    run_count = 0

  def test_default_procedure(self):
    try:
      loop.run()
    except Exception as error:
      self.fail("Implementation raised exception for default " +
          "procedure: " + str(error))

  def test_default_guard(self):
    global run_count

    loop.run(procedure=incrementor_procedure)
    self.assertEqual(run_count, 0)

  def test_run_twice_guard(self):
    global run_count

    loop.run(exit_guard=run_twice_guard,
      procedure=incrementor_procedure)

    self.assertEqual(run_count, 2)

  def test_mutation_of_game_state(self):
    global game_state

    loop.run(exit_guard=game_state_guard,
      procedure=game_state_mutator_procedure,
      game_state=game_state)

    self.assertEqual(game_state['run_count'], 3)
