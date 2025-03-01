
accept_words = ['accept', 'agree', 'confirm', 'consent', 'allow', 'accept1', 'accept2', 'accept3']
non_acceptable = ['disagree']

reject_words = ['reject', 'disagree', 'decline', 'deny', 'refuse', 'reject1', 'reject2']

setting_words = ['setting', 'manage', 'option', 'choice', 'purpose', 'preference', 'customize', 'configur']

login_words = ['login', 'einloggen']

words = {
    'en': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'accept',
        'agree': 'agree',
        'confirm': 'confirm',
        'consent': 'consent',
        'allow': 'allow',
        'accept1': 'continue',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'reject',
        'disagree': 'disagree',
        'decline': 'decline',
        'deny': 'deny',
        'refuse': 'refuse',
        'reject1': 'disable',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': 'personalised',
        'policy': 'policy',
        'privacy': 'privacy',
        'privacy policy': 'privacy policy',
        'legitimate interest': 'legitimate interest',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'de': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'akzeptieren',
        'agree': 'stimme zu',
        'confirm': 'bestätigen',
        'consent': 'consent',
        'allow': 'allow',
        'accept1': 'zustimmen',
        'accept2': 'annehmen',
        'accept3': 'akzeptiere',
        'reject': 'ablehnen',
        'disagree': 'oneens',
        'decline': 'afnemen',
        'deny': 'weigeren',
        'refuse': 'weigeren',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'einstellungen',
        'manage': 'verwalten',
        'option': 'option',
        'choice': 'auswahl',
        'purpose': 'zwecke',
        'preference': 'präferenz',
        'customize': 'anpassen',
        'configur': 'konfigurieren',
        'partner': 'partner',
        'personalised': 'personalisiert',
        'policy': 'politik',
        'privacy': 'datenschutz',
        'privacy policy': 'datenschutzerklärung',
        'legitimate interest': 'berechtigtes Interesse',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'es': {
        'cookies': 'cookies',
        'cookies1': 'cookies1',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'aceptar',
        'agree': 'acordar',
        'confirm': 'confirmar',
        'consent': 'consentir',
        'allow': 'permitir',
        'accept1': 'acept',
        'accept2': 'acceptar ',
        'accept3': 'acordar',
        'reject': 'rechazar',
        'disagree': 'desacuerdo',
        'decline': 'declive',
        'deny': 'negar',
        'refuse': 'rechazar',
        'reject1': 'deshabilitar',
        'reject2': 'rechazarlas',
        'setting': 'ajuste',
        'manage': 'administrar',
        'option': 'opcione',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preferencia',
        'customize': 'personalizar',
        'configur': 'configur',
        'partner': 'socio',
        'personalised': 'personalizado',
        'policy': 'política',
        'privacy': 'privacidad',
        'privacy policy': 'política de privacidad',
        'legitimate interest': 'interés legítimo',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'it': {
        'cookies': 'cookies',
        'cookies1': 'cookies1',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'accetta',
        'agree': 'concordare',
        'confirm': 'conferma',
        'consent': 'consenso',
        'allow': 'permettere',
        'accept1': 'accett',
        'accept2': 'acconsento',
        'accept3': 'accept3',
        'reject': 'rifiuta',
        'disagree': 'disagree',
        'decline': 'declino',
        'deny': 'negare',
        'refuse': 'rifiutare',
        'reject1': 'disabilita',
        'reject2': 'rifiuto',
        'setting': 'impostazione',
        'manage': 'gestisci',
        'option': 'opzion',
        'choice': 'scelt',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'personalizza',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': 'personalizz',
        'policy': 'politica',
        'privacy': 'privacy',
        'privacy policy': 'informativa sulla privacy',
        'legitimate interest': 'interesse legittimo',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'pt': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'aceitar',
        'agree': 'concordo',
        'confirm': 'confirmar',
        'consent': 'consentimento',
        'allow': 'permitir',
        'accept1': 'aceito',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'rejeitar',
        'disagree': 'discordo',
        'decline': 'declinar',
        'deny': 'negar',
        'refuse': 'recusar',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'gerenciar',
        'option': 'opções',
        'choice': 'escolha',
        'purpose': 'purpose',
        'preference': 'preferência',
        'customize': 'personalizar',
        'configur': 'configur',
        'partner': 'parceiro',
        'personalised': 'personalizado',
        'policy': 'política',
        'privacy': 'privacidade',
        'privacy policy': 'política de privacidade',
        'legitimate interest': 'interesse legítimo',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'zh': {
        'cookies': '承诺',
        'cookies1': 'cookies',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': '接受',
        'agree': '同意',
        'confirm': '确认',
        'consent': '承诺',
        'allow': '允许',
        'accept1': 'accept1',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': '拒绝',
        'disagree': '不同意',
        'decline': '拒绝',
        'deny': '拒绝',
        'refuse': '拒绝',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': '个性化',
        'policy': '政策',
        'privacy': '隐私',
        'privacy policy': '隐私政策',
        'legitimate interest': '合法权益',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'ru': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'принимаю',
        'agree': 'cогласен',
        'confirm': 'подтвердить',
        'consent': 'согласие',
        'allow': 'разрешить',
        'accept1': 'принимать',
        'accept2': 'принять',
        'accept3': 'accept3',
        'reject': 'отклонить',
        'disagree': 'не соглас',
        'decline': 'снижение',
        'deny': 'Запретить',
        'refuse': 'oтказаться',
        'reject1': 'не прин',
        'reject2': 'reject2',
        'setting': 'настройки',
        'manage': 'управлять',
        'option': 'параметры',
        'choice': 'выбор',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'партнер',
        'personalised': 'персонализированный',
        'policy': 'policy',
        'privacy': 'конфиденциальность',
        'privacy policy': 'политика конфиденциальности',
        'legitimate interest': 'законный интерес',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'ja': {
        'cookies': 'クッキー',
        'cookies1': 'cookies',
        'cookie': 'クッキー',
        'Cookie': 'クッキー',
        'accept': '受け入れる',
        'agree': '承認',
        'confirm': '確認',
        'consent': '同意',
        'allow': '許可する',
        'accept1': 'accept1',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': '拒絶',
        'disagree': '同意しない',
        'decline': 'decline',
        'deny': 'deny',
        'refuse': 'refuse',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'パートナー',
        'personalised': 'パーソナライズ',
        'policy': 'ポリシー',
        'privacy': 'プライバシー',
        'privacy policy': 'プライバシーポリシー',
        'legitimate interest': '正当な利益',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'fr': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'accepter',
        'agree': 'accord',
        'confirm': 'Confirmer',
        'consent': 'consent',
        'allow': 'autoriser',
        'accept1': 'accepte',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'rejeter',
        'disagree': 'pas d\'accord',
        'decline': 'déclin',
        'deny': 'refuser',
        'refuse': 'refuser',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'réglage',
        'manage': 'gérer',
        'option': 'option',
        'choice': 'choix',
        'purpose': 'purpose',
        'preference': 'préférence',
        'customize': 'personnaliser',
        'configur': 'configur',
        'partner': 'partenaire',
        'personalised': 'personnalisé',
        'policy': 'politique',
        'privacy': 'confidentialité',
        'privacy policy': 'politique de confidentialité',
        'legitimate interest': 'intérêt légitime',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'tr': {
        'cookies': 'çerezler',
        'cookies1': 'cookies',
        'cookie': 'çerezi',
        'Cookie': 'Çerezi',
        'accept': 'kabul',
        'agree': 'kabul',
        'confirm': 'onaylamak',
        'consent': 'izni',
        'allow': 'izin ver',
        'accept1': 'İzin',
        'accept2': 'izin',
        'accept3': 'accept3',
        'reject': 'reddet',
        'disagree': 'katılmıyorum',
        'decline': 'düşüş',
        'deny': 'inkar',
        'refuse': 'reddet',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'ortakları',
        'personalised': 'Kişiselleştirilmiş',
        'policy': 'gizlilik',
        'privacy': 'politikası',
        'privacy policy': 'gizlilik politikası',
        'legitimate interest': 'meşru menfaatt',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'fa': {
        'cookies': 'کوکی',
        'cookies1': 'cookies',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'accept',
        'agree': 'موافقم',
        'confirm': 'تایید',
        'consent': 'رضایت',
        'allow': 'می پذیرم',
        'accept1': 'accept1',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'مخالف',
        'disagree': 'disagree',
        'decline': 'decline',
        'deny': 'deny',
        'refuse': 'refuse',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': 'personalised',
        'policy': 'policy',
        'privacy': 'privacy',
        'privacy policy': 'privacy policy',
        'legitimate interest': 'legitimate interest',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    'sv': {
        'cookies': 'cookies',
        'cookies1': 'cookies2',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'acceptera',
        'agree': 'godkänn',
        'confirm': 'confirm',
        'consent': 'consent',
        'allow': 'tillåt',
        'accept1': 'accept1',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'reject',
        'disagree': 'disagree',
        'decline': 'decline',
        'deny': 'deny',
        'refuse': 'refuse',
        'reject1': 'disable',
        'reject2': 'reject2',
        'setting': 'inställningar',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': 'personalised',
        'policy': 'policy',
        'privacy': 'privacy',
        'privacy policy': 'privacy policy',
        'legitimate interest': 'legitimate interest',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
    # 'ar': {
    #     'cookies': 'ملفات تعريف',
    #     'cookies1': 'cookies',
    #     'cookie': 'cookie',
    #     'Cookie': 'Cookie',
    #     'accept': 'accept',
    #     'agree': 'agree',
    #     'confirm': 'confirm',
    #     'consent': 'consent',
    #     'allow': 'allow',
    #     'accept1': 'accept1',
    #     'accept2': 'accept2',
    #     'accept3': 'accept3',
    #     'reject': 'reject',
    #     'disagree': 'disagree',
    #     'decline': 'decline',
    #     'deny': 'deny',
    #     'refuse': 'refuse',
    #     'reject1': 'reject1',
    #     'reject2': 'reject2',
    #     'setting': 'setting',
    #     'manage': 'manage',
    #     'option': 'option',
    #     'choice': 'choice',
    #     'purpose': 'purpose',
    #     'preference': 'preference',
    #     'customize': 'customize',
    #     'configur': 'configur',
    #     'partner': 'partner',
    #     'personalised': 'personalised',
    #     'policy': 'policy',
    #     'privacy': 'privacy',
    #     'privacy policy': 'privacy policy',
    #     'legitimate interest': 'legitimate interest',
    #     'all': 'all',
    # },
    'ko': {
        'cookies': '쿠키',
        'cookies1': 'cookies',
        'cookie': 'cookie',
        'Cookie': 'Cookie',
        'accept': 'accept',
        'agree': 'agree',
        'confirm': 'confirm',
        'consent': 'consent',
        'allow': 'allow',
        'accept1': 'accept1',
        'accept2': 'accept2',
        'accept3': 'accept3',
        'reject': 'reject',
        'disagree': 'disagree',
        'decline': 'decline',
        'deny': 'deny',
        'refuse': 'refuse',
        'reject1': 'reject1',
        'reject2': 'reject2',
        'setting': 'setting',
        'manage': 'manage',
        'option': 'option',
        'choice': 'choice',
        'purpose': 'purpose',
        'preference': 'preference',
        'customize': 'customize',
        'configur': 'configur',
        'partner': 'partner',
        'personalised': 'personalised',
        'policy': 'policy',
        'privacy': 'privacy',
        'privacy policy': 'privacy policy',
        'legitimate interest': 'legitimate interest',
        'all': 'all',
        'login': 'login',
        'einloggen': 'einloggen',
    },
}
