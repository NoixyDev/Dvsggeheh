from flask import Flask, render_template, request

app = Flask(__name__)

TEXT = {
    "tr": {
        "nav_about": "Hakkımda", "nav_projects": "Projeler", "nav_goals": "Hedefler",
        "eyebrow": "BAĞIMSIZ YAZILIM GELİŞTİRİCİSİ",
        "headline": "Fikirleri projelere dönüştürüyorum.",
        "intro": "Merhaba, ben NoixyDev. Python ve Node.js ile yazılım projeleri geliştiriyorum. Özellikle Brawl Stars özel sunucu projelerine odaklanıyorum.",
        "projects_count": "40+ Proje", "experience": "2024'ten beri yazılım",
        "about_title": "Hakkımda", "about_body": "Yazılıma 2024 yılında ilgi duymaya başladım. İlk kodlarımı Python ile yazdım. Bugüne kadar 40'tan fazla proje geliştirdim; projelerimin neredeyse tamamı Brawl Stars ile ilgili. Çalışmalarımı bağımsız olarak ve tek başıma yürütüyorum.",
        "skills_title": "Kullandığım teknolojiler", "projects_title": "Projeler",
        "noixy_title": "Noixy Brawl", "noixy_body": "Python kullanarak kaliteli Brawl Stars özel sunucu projeleri geliştirme çalışmam. V11–V43 aralığındaki sürümler için projeler geliştirdim. Gelecekte daha yeni sürümleri hedefliyorum.",
        "other_title": "Diğer çalışmalar", "other_body": "Brawl Stars ekosistemiyle ilgili farklı Python ve Node.js projeleri. Toplam proje sayısı 40'ın üzerinde.",
        "goals_title": "Gelecek hedeflerim", "goals_body": "En büyük hedefim, gerçek zamanlı Online Battles sistemine sahip bir özel sunucu geliştirmek. Uzun vadede profesyonel yazılım geliştiricisi olmak ve kendi yazılım şirketimi kurmak istiyorum.",
        "interests_title": "Oyun dünyası", "interests_body": "Brawl Stars'ı yaklaşık 5 yıldır oynuyorum. En sevdiğim karakter Mortis. Boş zamanlarımda oyun oynuyor ve özel sunucu projeleri geliştiriyorum.",
        "footer": "NoixyDev tarafından tutkuyla geliştirildi."
    },
    "en": {
        "nav_about": "About", "nav_projects": "Projects", "nav_goals": "Goals",
        "eyebrow": "INDEPENDENT SOFTWARE DEVELOPER",
        "headline": "Turning ideas into projects.",
        "intro": "Hello, I'm NoixyDev. I build software projects with Python and Node.js, with a particular focus on Brawl Stars private-server projects.",
        "projects_count": "40+ Projects", "experience": "Building since 2024",
        "about_title": "About me", "about_body": "I became interested in software development in 2024 and wrote my first code in Python. Since then, I have built more than 40 projects, almost all related to Brawl Stars. I work independently and develop my projects on my own.",
        "skills_title": "Technologies", "projects_title": "Projects",
        "noixy_title": "Noixy Brawl", "noixy_body": "A project focused on creating quality Brawl Stars private-server experiences with Python. I have developed projects for versions V11–V43 and may target newer versions in the future.",
        "other_title": "Other work", "other_body": "A range of Python and Node.js projects related to the Brawl Stars ecosystem. More than 40 projects in total.",
        "goals_title": "Future goals", "goals_body": "My biggest goal is to develop a private server with a real-time Online Battles system. In the long term, I want to become a professional software developer and start my own software company.",
        "interests_title": "Gaming", "interests_body": "I've been playing Brawl Stars for around five years. My favourite brawler is Mortis. In my free time, I play games and work on private-server projects.",
        "footer": "Made with passion by NoixyDev."
    },
    "ru": {
        "nav_about": "Обо мне", "nav_projects": "Проекты", "nav_goals": "Цели",
        "eyebrow": "НЕЗАВИСИМЫЙ РАЗРАБОТЧИК",
        "headline": "Превращаю идеи в проекты.",
        "intro": "Привет! Я NoixyDev. Я создаю программные проекты на Python и Node.js, особенно проекты частных серверов Brawl Stars.",
        "projects_count": "40+ проектов", "experience": "Разработка с 2024 года",
        "about_title": "Обо мне", "about_body": "Я заинтересовался программированием в 2024 году. Свой первый код я написал на Python. С тех пор я создал более 40 проектов, почти все из которых связаны с Brawl Stars. Я работаю самостоятельно и разрабатываю проекты в одиночку.",
        "skills_title": "Технологии", "projects_title": "Проекты",
        "noixy_title": "Noixy Brawl", "noixy_body": "Проект по созданию качественных частных серверов Brawl Stars на Python. Я разрабатывал проекты для версий V11–V43 и в будущем планирую работать с более новыми версиями.",
        "other_title": "Другие работы", "other_body": "Различные проекты на Python и Node.js, связанные с экосистемой Brawl Stars. Всего создано более 40 проектов.",
        "goals_title": "Будущие цели", "goals_body": "Моя главная цель — создать частный сервер с системой онлайн-сражений в реальном времени. В будущем я хочу стать профессиональным разработчиком и открыть собственную IT-компанию.",
        "interests_title": "Игры", "interests_body": "Я играю в Brawl Stars около пяти лет. Мой любимый боец — Мортис. В свободное время я играю и работаю над проектами частных серверов.",
        "footer": "Создано с увлечением NoixyDev."
    }
}

@app.route("/")
def home():
    lang = request.args.get("lang", "tr").lower()
    if lang not in TEXT:
        lang = "tr"
    return render_template("index.html", t=TEXT[lang], lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
