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
    "Text": "Post Attack",
    "Enabled": false
  },
```

  Then, change the false to true, so it ends up like this:

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

We welcome your contributions in form of pull requests. You may create new issues to discuss the translations with other translators. Please note that issues not related to translation may be deleted without notice!

![3]

## Don't know Japanese but still want to contribute?

If you don't understand Japanese, but still want to help out, you can look over the translated lines and make sure all grammar and spelling is correct. (US English, please!)

## Message ID Mappings

You can refer to NovaParse's [Export JSON](https://github.com/Arks-Layer/Nova-Tools/blob/master/NovaParse/Export.json) file for a reference of RMD Message ID ranges. If you find any that seem incorrect or that need investigating, feel free to point them out in an issue or in the Discord channel.
