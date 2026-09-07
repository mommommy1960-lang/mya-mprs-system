from mprs import Command, SafetyController, SafetyState


def command(**changes):
    data = dict(
        command_id="1", purpose="victim_extraction", force=0.5,
        duration_ms=1000, location=(5.0, 5.0), signed=True,
    )
    data.update(changes)
    return Command(**data)


def test_bounded_rescue_simulation_is_allowed():
    controller = SafetyController((0, 0, 10, 10))
    controller.arm_simulation()
    assert controller.authorize(command()) is True
    assert controller.verify_audit() is True


def test_hardware_weapon_and_unsigned_paths_are_absent():
    controller = SafetyController((0, 0, 10, 10))
    controller.arm_simulation()
    assert controller.authorize(command(simulation=False)) is False
    assert controller.authorize(command(purpose="weapon_targeting")) is False
    assert controller.authorize(command(signed=False)) is False


def test_limits_and_geofence_fail_closed():
    controller = SafetyController((0, 0, 10, 10))
    controller.arm_simulation()
    assert controller.authorize(command(force=2.0)) is False
    assert controller.authorize(command(duration_ms=9000)) is False
    assert controller.authorize(command(location=(99.0, 99.0))) is False


def test_watchdog_enters_frozen_neutral_state():
    controller = SafetyController((0, 0, 10, 10))
    controller.arm_simulation()
    controller.set_watchdog(False)
    assert controller.state is SafetyState.FROZEN
    assert controller.authorize(command()) is False
