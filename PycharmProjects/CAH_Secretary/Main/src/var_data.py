from os import environ

token = environ.get('TOKEN')

roles_str = None
roles_set = set()
restricted_roles = {
    "Accepted",
    "Committed"
}

locked_roles = {
                "Admin",
                "Dyno",
                "UB3R-B0T",
                "Moderator",
                "Partner",
                "Admin Emeritus",
                "Mod Emeritus",
                "Muted",
                "Verified",
                "Committed",
                "Accepted",
                "Admissions",
                "Contributor",
                "Pulitzer Winner",
                "Bot Commander",
                "Bot",
                "ApplyingToCollegeBot",
                "Cyan",
                "(ﾉ◕ヮ◕)ﾉ✧･ﾟ*✧spoo.py✧*･ﾟ✧ヽ(◕ヮ◕)ﾉ",
                "Tatsumaki",
                "MathBot",
                "Botless",
                "IT Guy",
                "@everyone"
}