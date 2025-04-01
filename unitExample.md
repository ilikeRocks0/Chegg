UnitData:
    Name: Villager
    Cost: 0
    Moves: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    Attacks: [
        AttackType: attack_single
        Attacks: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        Modifiers: move_on_attack
    ]
    Death: lose_game


UnitData:
    Name: Zombie
    Cost: 1
    Moves: [(-1,1), (0,1), (1,1)]
    Attacks: [
        AttackType: attack_single
        Attacks: [(1,0), (-1,0), (0,1), (0,-1)]
    ]

UnitData:
    Name: Creeper
    Cost: 1
    Moves: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    Attacks: [
        AttackType: attack_group
        Attacks: [[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]
    ]