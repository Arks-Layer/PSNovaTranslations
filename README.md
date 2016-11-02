[3]: https://github.com/Arks-Layer/PSO2JPTranslations/blob/master/resources/rightmeow.png

<p align="center">
  <img src="https://github.com/Arks-Layer/PSNovaTranslations/blob/master/resources/Phantasy-Star-Nova-Logo.png" alt="PS Nova Logo"/>
</p>

# PS: Nova Translations
Welcome to the PS: Nova Translations Github Repository.

This repository is dedicated to translating PS: Nova game texts from Japanese to English. We hope our disclosing of game texts and opening this repository will pave a quicker way for non-Japanese speaking ARKS to enjoy the game in their native languages in the future.

<i>While we appreciate the efforts of those who don't speak Japanese (through Google translate and the like), we would like for only those who have a grasp of the Japanese language to submit edits to those. ありがとう～ (*＾▽＾)／</i>

## Contributions

 1. Click the file you want to edit
 2. Click the pencil icon
 3. Edit the file to your heart's content!
 4. Write a brief summary of the changes at the bottom of the page
 5. Hit "Create a new branch for this commit and start a pull request." (<b>DO NOT COMMIT DIRECTLY TO MASTER.</b>)
 6. Your PR request will be reviewed and accepted or denied. (Your changes will also be posted to the discord chat.)

 
##Editing process

Please put your translation in the "Text" field like so:
  
```
  "310040": {
    "OriginalText": "ポストアタック",
    "Text": "Post Attack"
  },
```

  Then, add a comma to the end of your translation, and put "    "Enabled": true" on the next line, so it ends up like this:

```
  "310040": {
    "OriginalText": "ポストアタック",
    "Text": "Post Attack",
    "Enabled": true
  },
```
Please note that there may be "weird" things in the text! For example, "[c]" and "[n]". The n is a "new line".

<b><i><u>PLEASE LEAVE THESE TAGS IN THERE.</b></i></u>

The [ruby] tag indicates that the text inside of it will be above the enclosed text. For example:

```
msg_100000010010013.rmd:
お願い……わたしの[ruby ほし]惑星[/ruby]を……助けて。
```

will show up as:

```
               ほし
お願い……わたしの惑星を……助けて。
```

<b><i><u>PLEASE LEAVE THESE TAGS IN THERE.</b></i></u>

We welcome your contributions in form of pull requests. You may create new issues to discuss the translations with other translators. Please note that issues not related to translation may be deleted without notice.

![3]

## Don't know Japanese but still want to contribute?

If you don't understand Japanese, but still want to help out, you can look over the translated lines and make sure all grammar and spelling is correct. (US English, please!)

## Message ID Mappings

```
msg_10XXX.rmd is status stuff (check on this)
msg_11XXX.rmd is main menu (start menu) stuff
msg_2XXXX.rmd is character stuff (current class, learning techs/arts, waking people from deep sleep, room? placement, crew assignment, maybe error messages related to those as well?,  etc)
msg_22XXX.rmd is button configuration stuff? (Jump, settings, etc)
msg_23XXX.rmd has various class stuff and party strings.
msg_24XXX.rmd seems to have field strings (revival and such, gigants, etc)
msg_3XXXX.rmd is NPC names (done)
msg_4XXXX.rmd are dummy strings?
msg_5XXXX.rmd are skill names (War cry, HP Up 1, etc)
msg_6XXXX.rmd are skill descriptions
msg_7XXXX.rmd is skill names, but worded differently (Maybe imported directly from PSO2? It says to delete them and put the modified versions in msg_50000, so maybe.)
msg_8XXXX.rmd is skill descriptions, but worded differently (Maybe imported directly from PSO2? It says to delete them and put the modified versions in msg_50000, so maybe.) 
msg_9XXXX.rmd is weapons (mostly done) (on github)
msg_10XXXX.rmd is weapon descriptions (check on this)
msg_11XXXX.rmd is enemy cores? (on github)
msg_12XXXX.rmd is enemy core? descriptions
msg_13XXXX.rmd is weapons too? ã‚¢ãƒ«ãƒ‘ã‚·ã‚¶ãƒ¼ (More weapons?)
msg_14XXXX.rmd is weapon descriptions too?
msg_15XXXX.rmd is affixes (on github)
msg_16XXXX.rmd is affix descriptions
msg_17XXXX.rmd is misc messages (weapon creation, item placement, character customization, etc)
msg_18XXXX.rmd is enemy names (on github)
msg_19XXXX.rmd is Gacha NPCs???
msg_20XXXX.rmd is... I have no fucking idea, window titles?
msg_21XXXX.rmd is objectives (field) (on github)
msg_23XXXX.rmd is mission descriptions
msg_24XXXX.rmd is leveling up facilities?
msg_25XXXX.rmd is descriptions for the facilities?
msg_26XXXX.rmd are... strings about "please come here and do this"/planetwide transmissions/in-field communications etc?
msg_28XXXX.rmd are... challenges? "Defeat enemies using only the assault rifle/Don't die/Don't get hit/etc"
msg_29XXXX.rmd are promise orders?
msg_30XXXX.rmd are collection quests?
msg_31XXXX.rmd is shield stuff (Mostly done)
msg_33XXXX.rmd is clothing (Done)
msg_34XXXX.rmd are clothing descriptions
msg_35XXXX.rmd are Gran Items (ã‚°ãƒ©ãƒ³ãƒ”ãƒ¼ã‚¹, Gran Piece, etc)
msg_36XXXX.rmd are Gran item descriptions
msg_37XXXX.rmd is items (monomates, etc)
msg_38XXXX.rmd is item descriptions
msg_39XXXX.rmd is boost items/scapedolls (on github)
msg_40XXXX.rmd is descriptions for boost items (on github)
msg_41XXXX.rmd is Story chapter names?
msg_43XXXX.rmd is button text (cancel, accept, sort, etc)
msg_44XXXX.rmd has hair/other stuff? (on github)
msg_50XXXX.rmd is default body types and voices
msg_51XXXX.rmd are styles
msg_52XXXX.rmd are characteristics
msg_53XXXX.rmd are NPC comments ("Call on me when you need me!" etc)
msg_54XXXX.rmd are Crew types
msg_55XXXX.rmd is Food? (on github)
msg_56XXXX.rmd are Gran Arts (on github)
msg_57XXXX.rmd are Gran Arts descriptions (on github)
msg_58XXXX.rmd are Techniques (on github)
msg_59XXXX.rmd are Technique descriptions (on github)
msg_60XXXX.rmd are Lobby Actions (on github)
msg_61XXXX.rmd are Lobby Action descriptions (on github)
msg_62XXXX.rmd are random field strings? 
msg_63XXXX.rmd is food item descriptions? (on github)
msg_64XXXX.rmd are status effects
msg_65XXXX.rmd is crew descriptions
msg_66XXXX.rmd are class descriptions
msg_67XXXX.rmd are... no freaking idea.
msg_68XXXX.rmd are same as above, no idea.
msg_69XXXX.rmd are descriptions of the ships weapons?
msg_70XXXX.rmd are quest/mission objectives?
msg_71XXXX.rmd are quest descriptions?
msg_73XXXX.rmd are search/survey team strings
msg_74XXXX.rmd are bonus effects?
msg_751XXX.rmd has field NPC names?
msg_752XXX.rmd is credits
msg_77XXXX.rmd is tutorial titles (yay!)
msg_78XXXX.rmd is tutorial window text
msg_79XXXX.rmd are area names
msg_80XXXX.rmd are the loading tips
msg_81XXXX.rmd are the story summary entries (and later their titles)
msg_82XXXX.rmd are increasing stats/affixes?
```
