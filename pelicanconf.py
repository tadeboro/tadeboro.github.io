AUTHOR = "Tadej Borovšak"
SITENAME = "Little silly things"
SITEURL = ""

PATH = "content"
THEME = "theme"

TIMEZONE = "UTC"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

SLUGIFY_SOURCE = "basename"

STATIC_PATHS = [""]
DIRECT_TEMPLATES = ["index", "tags"]
TAGS_SAVE_AS = "tags/index.html"
for i in ("article", "tag"):
    globals()[f"{i.upper()}_URL"] = i + "s/{slug}/"
    globals()[f"{i.upper()}_SAVE_AS"] = i + "s/{slug}/index.html"
for i in ("category", "page", "author"):
    globals()[f"{i.upper()}_SAVE_AS"] = ""

DEFAULT_LANG = "en"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
