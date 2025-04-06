{
    Villager:
    {
        name: Villager
        cost: 0
        moves: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        attacks: [
            AttackType: attack_single
            AttacksList: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            modifiers: move_on_attack
        ]
        death: lose_game
        modifiers: extra_move_cost
    }


    Zombie:
    {
        Name: Zombie
        Cost: 1
        Moves: [(-1,1), (0,1), (1,1)]
        Attacks: [
            AttackType: attack_single
            Attacks: [(1,0), (-1,0), (0,1), (0,-1)]
        ]
    }
    
    Creeper:
    {
        Name: Creeper
        Cost: 1
        Moves: [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        Special: [
            SpecialType: explode
            SpecialsLists: [(0,0)]
        ]
        Death: explode
    }

}
