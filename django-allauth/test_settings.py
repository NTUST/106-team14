SECRET_KEY = 'psst'
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ROOT_URLCONF = 'allauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.asana',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.basecamp',
    'allauth.socialaccount.providers.battlenet',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.box',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.douban',
    'allauth.socialaccount.providers.doximity',
    'allauth.socialaccount.providers.draugiem',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dropbox_oauth2',
    'allauth.socialaccount.providers.dwolla',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.eveonline',
    'allauth.socialaccount.providers.evernote',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.fivehundredpx',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.mailchimp',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.robinhood',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.slack',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.stripe',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twentythreeandme',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.untappd',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.windowslive',
    'allauth.socialaccount.providers.xing'
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

STATIC_ROOT = '/tmp/'  # Dummy
STATIC_URL = '/static/'