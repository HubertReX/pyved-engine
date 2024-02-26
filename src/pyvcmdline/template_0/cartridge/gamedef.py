from . import pimodules


pyv = pimodules.pyved_engine
pyv.bootstrap_e()
pyg = pyv.pygame


@pyv.declare_begin
def init_game(vmst=None):
    pyv.init(wcaption='Néant')


@pyv.declare_update
def upd(time_info=None):
    pyv.vars.gameover=True


@pyv.declare_end
def done(vmst=None):
    pyv.close_game()
    print('gameover!')
