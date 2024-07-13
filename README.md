<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>



<body>

<style>
    #copy_btn{
        font-family: "Times New Roman", Georgia, Serif;
        font-size: 18px;
        cursor: pointer;
        background-color: transparent;
        border: none;
    }
</style>

    <h1 align="center">POST BOT</h1>
    Postbit is a Telegram bot created to automatically post content.
    <br>
    <br>

    <b>Usage:</b><br>
    To use the bot, you need to log in to <b>Telegram</b> and create your own bot using 
    <button id="copy_btn" onclick="copy_ID('@BotFather')"><b><u>@BotFather</u></b>.</button>
    <br>
    Insert the token of the created bot into the value <b>main.py -> API_TOKEN</b>.<br><br>
    It is also necessary to create 2 channels:<br>
    the source channel, from where the message will be copied once at the specified time;<br>
    and the target channel, where a post will be created once at the specified time.<br><br>
    Then specify their IDs accordingly in <b>handler.py -> TARGET_CHANNEL_ID</b> and <b>handler.py -> SOURCE_CHANNEL_ID</b>. <br>
    To specify the delay of posts, you must specify a value for handlers.py -> POST_DELAY<br>


    Now you should log into your bot and write the 
    <button id="copy_btn" onclick="copy_ID('/start')"><b><u>/start</u></b>.</button> command.<br>
    The bot will greet you and ask you to enter your password.<br>
    The default password is 
    <button id="copy_btn" onclick="copy_ID('Password')"><b><u>"Password"</u></b>.</button>
    , but it can be changed by changing the variable <b>handlers.py -> ADMIN_PASSWORD</b>.<br><br>

    After the correct password is entered, the bot will inform you about it and offer 4 options:
    <ul>
        <li>Login again - Enter the password again.</li>
        <li>Post now - Make a post now.</li>
        <li>Start posting - Start making posts with the specified delay.</li>
        <li>Stop posting - Stop making posts with the specified delay</li>
    </ul>

    
    <script>
        function copy_ID(txt) {
            var inp = document.createElement('input')
            inp.value = txt;
            document.body.appendChild(inp);
            inp.select();
            document.execCommand("copy");
            alert("Copied the text: " + inp.value);
            document.body.removeChild(inp)
        }
    </script>
</body>
</html>