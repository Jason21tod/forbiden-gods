execute as @s if block ~ ~ ~ minecraft:air run execute as @s[nbt={ActiveEffects:[{"forge:id": "minecraft:slowness"}]}] run tp ~ ~-1 ~
execute as @s if block ~ ~ ~ minecraft:air run execute as @s[nbt={ActiveEffects:[{"forge:id": "minecraft:slowness"}]}] run effect give @s footwork:unsteady 3 0 false
execute as @s if block ~ ~ ~ minecraft:air run execute as @s[nbt={ActiveEffects:[{"forge:id": "minecraft:slowness"}]}] run effect give @s minecraft:mining_fatigue 3 1 false
execute as @s if block ~ ~ ~ minecraft:air run execute as @s[nbt={ActiveEffects:[{"forge:id": "minecraft:slowness"}]}] run effect clear @s minecraft:slowness

