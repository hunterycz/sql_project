SELECT_ALL = '''
SELECT *
FROM charactercreator_character
'''

TOTAL_CHARACTERS = '''
SELECT COUNT(character_id)
FROM charactercreator_character
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
FROM armory_item
'''
