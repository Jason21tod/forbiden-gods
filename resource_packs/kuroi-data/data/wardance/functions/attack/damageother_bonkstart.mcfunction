execute as @s if block ~ ~ ~ #minecraft:mineable/pickaxe run function wardance:attack/damageother_break
execute as @s if block ~ ~ ~ #minecraft:mineable/shovel run function wardance:attack/damageother_break
execute as @s if block ~ ~ ~ minecraft:air run execute unless data entity @p {ActiveEffects:[{"forge:id": "minecraft:slowness"}]} run function wardance:attack/damageother_mildstun
execute as @s if block ~ ~ ~ minecraft:air run execute if data entity @p {ActiveEffects:[{"forge:id": "minecraft:slowness"}]} run function wardance:attack/damageother_bonkeffect
