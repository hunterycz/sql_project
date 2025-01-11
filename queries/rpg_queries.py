SELECT_ALL = '''
SELECT *
FROM charactercreator_character;
'''

TOTAL_CHARACTERS = '''
SELECT COUNT(character_id)
FROM charactercreator_character;
'''

TOTAL_SUBCLASS = '''
SELECT
	(SELECT COUNT(*)
	FROM charactercreator_mage mage
	INNER JOIN charactercreator_character ccc
	ON mage.character_ptr_id = ccc.character_id) AS Mage_Count,
	(SELECT COUNT(*)
	  FROM  charactercreator_cleric cleric
	  INNER JOIN charactercreator_character ccc
	  ON cleric.character_ptr_id = ccc.character_id) AS Cleric_Count,
	 (SELECT COUNT(*)
	   FROM charactercreator_thief thief
	   INNER JOIN charactercreator_character ccc
	   ON thief.character_ptr_id = ccc.character_id) AS Thief_Count,
	(SELECT COUNT(*)
	  FROM charactercreator_fighter fighter
	  INNER JOIN charactercreator_character ccc
	  ON fighter.character_ptr_id = ccc.character_id) AS Fighter_Count;
'''

TOTAL_ITEMS = '''
SELECT COUNT(*) AS total_items
FROM armory_item;
'''

TOTAL_WEAPONS = '''
SELECT COUNT(*) AS total_weapons
FROM armory_weapon;
'''

TOTAL_NON_WEAPONS = '''
SELECT COUNT(*) AS non_weapons
FROM armory_item AS ai
LEFT JOIN armory_weapon AS aw
ON ai.item_id = aw.item_ptr_id
WHERE power IS NULL;
'''

CHARACTER_ITEMS = '''
SELECT character_id, COUNT(*) AS character_items
FROM charactercreator_character_inventory AS ccc_inv
INNER JOIN armory_item AS ai
ON ccc_inv.item_id = ai.item_id
GROUP BY ccc_inv.character_id;
'''

CHARACTER_WEAPONS = '''
SELECT character_id, COUNT(*) AS character_weapons
FROM charactercreator_character_inventory AS ccc_inv
INNER JOIN armory_weapon AS aw
ON ccc_inv.item_id = aw.item_ptr_id
GROUP BY ccc_inv.character_id
'''

AVG_CHARACTER_ITEMS = '''
SELECT ROUND(AVG(character_items), 2) AS avg_items_per_character
FROM (
			SELECT COUNT(*) AS character_items
			FROM charactercreator_character_inventory AS ccc_inv
			INNER JOIN armory_item AS ai
			ON ccc_inv.item_id = ai.item_id
			GROUP BY ccc_inv.character_id
			) AS item_counts;

'''

AVG_CHARACTER_WEAPONS = '''
SELECT ROUND(AVG(character_weapons), 2) AS avg_weapons_per_character
FROM (
				SELECT COUNT(*) AS character_weapons
				FROM charactercreator_character_inventory AS ccc_inv
				INNER JOIN armory_weapon AS aw
				ON ccc_inv.item_id = aw.item_ptr_id
				GROUP BY ccc_inv.character_id
				) AS weapon_counts
'''

SELECT_ALL_INVENTORY = '''
SELECT *
FROM charactercreator_character_inventory
'''

SELECT_ALL_WEAPONS = '''
SELECT *
FROM armory_weapon
'''

SELECT_ALL_MAGES = '''
SELECT *
FROM charactercreator_mage
'''

SELECT_ALL_THEIVES = '''
SELECT *
FROM charactercreator_thief
'''

SELECT_ALL_CLERIC = '''
SELECT *
FROM charactercreator_cleric
'''

SELECT_ALL_FIGHTER = '''
SELECT *
FROM charactercreator_fighter
'''

SELECT_ALL_NECROMANCER = '''
SELECT *
FROM charactercreator_necromancer
'''

SELECT_ALL_ITEMS = '''
SELECT *
FROM armory_item
'''

SELECT_ALL_MAGES_LIMIT_5 = '''
SELECT *
FROM charactercreator_mage
LIMIT 5;
'''

SELECT_ALL_THEIVES_LIMIT_5 = '''
SELECT *
FROM charactercreator_thief
LIMIT 5;
'''

SELECT_ALL_CLERIC_LIMIT_5 = '''
SELECT *
FROM charactercreator_cleric
LIMIT 5;
'''
