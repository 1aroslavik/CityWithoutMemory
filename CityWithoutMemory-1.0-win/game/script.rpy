default player_name = "..."

define lea = Character("Lea", color="#ffc8c8")
define bib = Character("Librarian", color="#ffc8c8")
define sil = Character("???", color="ffc8c8")
define eil = Character("Eilin", color="ffc8c8")
define doc = Character("Doctor", color = "ffc8c8")
define man = Character("Man", color = "ffc8c8")
define girl = Character("Girl", color = "ffc8c8")

image library = "scene/library.png"
image forest = "scene/forest.png"
image car = "scene/car.png"
image village = "scene/village.png"
image villageNight = "scene/villageNight.png"
image pit = "scene/pit.png"
image cafe = "scene/cafe.png"
image black = "scene/black.jpg"
image inpit = "scene/inpit.jpg"
image crest = "scene/crest.png"
image bedroom = "scene/bedroom.png"
image HospitalOn = "scene/HospitalOn.png"
image HospitalOff = "scene/HospitalOff.png"
image EilinOffice = "scene/EilinOffice.png"
image room = "scene/Room.png"
image roomRed = "scene/RoomRed.png"
image roomBlue = "scene/RoomBlue.png"
image testRoom = "scene/TeseRoom.png"

image ggN = "character/gg/ggNormal.png"
image ggVH = "character/gg/ggVeryHappy.png"
image ggA = "character/gg/ggAngry.png"
image ggS = "character/gg/ggScary.png"
image ggH = "character/gg/ggHappy.png"
image ggCloseEyesDB = "character/gg/ggcloseEyesDB.png"
image ggCloseEyesD = "character/gg/ggcloseEyesD.png"
image ggCloseEyes = "character/gg/ggCloseEyes.png"
image ggScarryDB = "character/gg/ggscarryDB.png"
image ggScarryD = "character/gg/ggscarryD.png"
image ggScarry = "character/gg/ggScarry.png"
image ggCryDB = "character/gg/ggcryDB.png"
image ggCryD = "character/gg/ggCryD.png"
image ggCry = "character/gg/ggCry.png"



image leaNS = "character/lea/leaNormalSmile.png"
image leaD = "character/lea/leaDied.png"
image leaS = "character/lea/leaScarry.png"
image leaSir = "character/lea/leaSerious.png"
image leaSmile = "character/lea/leaSmile.png"
image leaP1 = "character/lea/LeaPt1Serious.png"
image leaDis= "character/lea/LeaDissatisfied.png"
image leaVeryAn= "character/lea/LeaVeryAngry.png"
image leaVeryHap= "character/lea/LeaVeryHappy.png"
image leaSad = "character/lea/LeaSad.png"
image leaAngry = "character/lea/leaAngry.png"

image EilCosAston = "character/eilin/ECastonishment.png"
image EilCosDis = "character/eilin/ECdissatisfied.png"
image EilCosGrin = "character/eilin/ECgrin.png"
image EilCosNeutral = "character/eilin/ECneutral.png"
image EilCosSilh = "character/eilin/ECsilhouette.png"
image EilCosSmile = "character/eilin/ECsmile.png"
image EilDreAston = "character/eilin/EDastonishment.png"
image EilDreDis = "character/eilin/EDdissatisfied.png"
image EilDreGrin = "character/eilin/EDgrin.png"
image EilDreNeutral = "character/eilin/EDneutral.png"
image EilDreSmile = "character/eilin/EDsmile.png"


image celBack = "character/celBack.png"
image celFont = "character/celFont.png"
image sill = "character/sill.png"
image DocNeu = "character/DocNeuthral.png"
image DocDiss = "character/DocDissatisfied.png"
image DocSmile = "character/DocSmile.png"
image GirlFalse = "character/GirlFalse.png"
image GirlNeu = "character/GirlNeu.png"
image GirlTruth = "character/GirlTruth.png"
image GirlScarry = "character/GirlScarry.png"
image men= "character/men.png"



label start:

    stop music fadeout 1.0
    play music "audio/cafe.mp3" fadein 1.0
    scene library
    with fade

    $ player_name = renpy.input("Введите имя главного героя:")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Аноним"

    $ gg = Character(player_name, color="#c8c8ff")

    show ggN at center
    gg " Надеюсь, сегодня я её найду. "
    hide ggN

    show ggA at center
    gg " Сколько уже можно, как ни приду — постоянно кто-то её забирает. "
    gg " Я обязан наконец её прочитать. "
    gg " Да, было бы удобнее просто её купить, но финансы бедного студента не позволяют. "
    gg " Господи, не могу себе позволить несчастную книгу... "
    hide ggA

    show ggN at center
    gg " Ну всё, хватит страдать… "
    gg " Нельзя позволять портить самому себе такой хороший день. "
    gg " Запах кофе и старых книг, шум дождя за окном, время будто остановилось. "
    hide ggN

    show ggH at left

    gg " Неужели… Вот она. "
    
    "Ты потянулся за потрёпанной книгой на нижней полке, но твои пальцы столкнулись с чьими-то тёплыми ладонями."
    "Ты вздрогнул и резко отдёрнул руку."

    show leaNS at right

    lea "Ой..."
    lea "Извини... ты тоже её хотел?"
    gg "Да..."

    
    menu:
        "Уступить книгу":
            jump leaveBook
        "Забрать книгу":
            jump takeBook

    label leaveBook:

        gg "Забирай, я подыщу что-то другое."
        lea "Правда?!!!"
        lea "Спасибо огромное, я долго ждала возможности её прочитать!"
        gg "Без проблем."
        lea "Могу ли я угостить тебя кофе за твою доброту?"
        menu:
            "Согласиться":
                jump coffeBreakY
            "Отказаться":
                jump coffeBreakN



    label takeBook:
        hide ggH
        show ggA at left
        hide leaNS 
        show leaP1 at right
        gg "Нет, извини, я спешу."
        lea "Ладно, спасибо ещё раз!"
        hide leaP1
        "Ты попрощался и снова окунулся в запах старых книг"
        return

    label coffeBreakN:
        hide leaNS
        hide ggH
        show leaP1 at right
        show ggN at left
        gg "Нет, извини, я спешу."
        lea "Ладно, спасибо ещё раз!"

        hide leaNS
        "Ты попрощался и снова окунулся в запах старых книг, решив найти себе что-то другое для чтения."
        return

    label coffeBreakY:

        gg "Да, с удовольствием."
        scene cafe
        show leaNS at right
        show ggH at left
        lea "Ты просто мой спаситель."
        hide ggH 
        show ggN at left
        gg "О чём ты?"
        lea "Я пишу диплом, мне очень нужна эта книга для исследования. Не знаю, что бы я делала, если бы ты не уступил."
        
        hide ggN
        show ggH at left
        gg "Очень рад помочь."
        lea "Я так и не знаю имени своего спасителя..."
        gg "[player_name]"
        lea "Очень приятно, меня зовут Лея."
        lea "Будем знакомы."

        lea "Так а тебе зачем эта книга?"
        gg "Это последняя часть трилогии, я давно пытаюсь выхватить момент, когда она будет здесь, чтобы забрать её."
        gg "Но каждый раз кто-то успевает быстрее..."
        lea "Теперь мне стыдно, что я тебя лишаю возможности узнать, чем всё закончится."
        lea "Там действительно очень завораживающий переворот..."
        hide ggH
        show ggA at left
        gg "Нееет, стой!!!"
        lea "Хахах, извини, просто я беру её уже в третий раз."
        lea "Первые два — просто потому что очень люблю эту серию, а сейчас вот решила писать по ней дипломную работу."
        hide ggA
        show ggH at left
        gg "Очень интересно."
        lea "Всё же мне очень жаль..."
        lea "Может прочтём её вместе...?"
        gg "А ты случайно не из тех, кто читает всё с карандашом и блокнотом для записей?"
        
        hide leaNS
        show leaP1 at right
        lea "Да... Вообще всё именно так..."
        lea "Дождь так и не заканчивается, если ты не спешишь, можем начать читать здесь."
        lea "Будет интересно увидеть твои эмоции от первого прочтения."
        
        hide leaP1
        show leaNS at right
        lea "Для тебя я сделаю исключение, и уберу свой блокнот подальше."
        gg "Это странно."
        lea "Почему же?"
        lea "Будем обсуждать и спорить."
        gg "Мне никогда не приходило в голову что-то подобное."
        gg "Думаю, стоит попробовать."
        hide leaNS
        hide ggH
        show leaP1 at right
        show ggN at left
        bib "Ребята, мы уже закрываемся."
        lea "Что? Уже?"
        lea "Так быстро время пролетело, я даже не заметила."
        hide leaP1
        hide ggN
        show leaNS at right
        show ggH at left
        gg "Да, спасибо за такой опыт, было действительно интересно обсуждать с тобой книгу."
        lea "Мне тоже, но это ведь ещё не конец, можем встретиться завтра."
        gg "А как же твой диплом?"
        lea "Время ещё есть, так что?"
        gg "Да, с удовольствием, завтра в это же время, но кофе уже с меня."
        lea "Хорошо, до встречи."
        gg "До встречи!"

        hide leaNS
        hide ggH       
        "Прошёл год"
        show leaSmile at right
        show ggH at left
        gg "Помнишь как мы впервые здесь встретились?"
        lea "Конечно, это невозможно забыть."
        gg "Да, если бы не та книга, не знаю, что бы я делал без тебя."
        lea "Да, без меня ты бы просто грустил..."
        gg "Да-да, я тебя тоже очень сильно люблю."
        hide leaSmile
        show leaAngry at right
        lea "Стой, а точно, это же было ровно год назад...?"
        hide leaAngry
        show leaSmile at right
        hide ggH
        show ggN at left
        lea "А тут всё так же, время будто бы остановилось."
        lea "Всё тот же запах кофе и старых книг, всё тот же звук дождя за окном..."
        gg "Ты выйдешь за меня?"
        hide leaSmile
        show leaVeryHap at right
        lea "ЧТО?"
        gg "Спрашиваю, ты выйдешь за меня...?"
        hide ggN
        show ggH at left
        lea "ААА... да, да, да! Конечно!"
        gg " Хорошо, что я тогда отдал ей эту книгу. Прошёл год, а кажется будто я знаю её всю жизнь. Господи, как же я рад быть с ней. "

        stop music fadeout 1.0
        play music "audio/car.mp3" fadein 1.0

        scene car
        show leaSad at right
        show ggN at left
        lea "Погода, конечно, не для поездок."
        gg "Я знаю, милая, но родители нас уже ждут."
        lea "Да, просто предчувствие нехорошее."
        gg "Не переживай, это просто паника перед свадьбой."
        lea "Да, наверное."
        gg "Ну что, поехали."
        lea "Да..."
        hide leaSad
        show leaSir at right
        lea "Дорогой, ты уверен, что мы правильно едем?"
        gg "Вроде по картам всё правильно. Если ты переживаешь — посмотри сама."
        lea "Странно, навигатор не работает, связи на телефоне тоже нет."
        gg "Как...? Мда, действительно странно. Но я помню дорогу."
        lea "Я включу радио, ты не против?"
        gg "Конечно, милая."

        stop music fadeout 1.0
        play music "audio/radio.mp3" fadein 1.0


        hide leaSir
        show leaS at right
        lea "Радио тоже не работает. Меня это пугает."
        gg "Не переживай, осталось совсем немного."
        stop music fadeout 1.0
        play music "audio/car.mp3" fadein 1.0

        "час спустя"
        hide leaS
        show leaSad at right
        gg "Дорога ни к чёрту. Не помню, чтобы тут было так много ям."
        lea "Давай остановимся, ветер становится только сильнее. Может переждём?"
        menu:
            "Остановится и переждать":
                jump stop
            "Ехать дальше":
                jump go
        label stop:
            stop music fadeout 1.0
            play music "audio/forest.mp3" fadein 1.0

            hide leaSad
            show leaS at right
            lea "Меня пугает вся эта ситуация."
            gg "Я знаю. Переждём и поедем дальше."
            lea "Даже не понятно сколько ждать, ещё и связи нет."
            gg "Я выйду и осмотрюсь."
            lea "Может, не стоит?"
            gg "Не переживай. Может удастся поймать сигнал, чтобы хоть примерно знать где мы."
            hide leaS
            show leaSad at right
            lea "Я пойду с тобой."
            gg "Хорошо, только аккуратнее."

            "Возвращаются через какое-то время. Двери машины открыты, внутри всё разбросано."
            hide leaSad
            show leaS at right
            hide ggN
            show ggA at left

            lea "Что случилось с нашей машиной?"
            menu:
                "Чёрт возьми, ты забыла закрыть двери?":
                    lea "Нет, я закрывала, я точно это помню."
                    gg "Я вижу как ты закрыла. И что нам теперь делать без вещей и денег, даже документов не осталось?"
                    lea "Я не виновата, хватит меня во всём обвинять."
                    gg "Садись в машину, поедем дальше."
                    jump CROSS

                "Видимо не стоит нам тут оставаться, садись и поедем дальше":
                    jump CROSS

            label CROSS:
                stop music fadeout 1.0
                play music "audio/car.mp3" fadein 1.0

                hide leaS
                hide ggA
                show leaSad at right
                show ggN at left
                menu:
                    "Поехать прямо":
                        jump goDir
                    "Поехать направо":
                        jump goRight
                    "Поехать налево":
                        jump goLeft
                    "Поехать назад":
                        jump goBack
       
        label go:
            gg "Проверь ещё раз, точно нет связи?"
            lea "Нет, ни навигатор, ни телефон, ни радио — ничего не работает."
            gg "Ладно, поедем просто прямо."
            gg "Перекрёсток? Я не помню, чтобы он тут был."
            jump CROSS

        label goDir:
            lea "Мы едем уже где-то 30 мин, точно куда-то приедем"
            gg "Да, я надеюсь"
            "еще 30 мин спустя" 
            hide ggN
            hide leaSad
            show leaVeryAn at right
            show ggA at left
            gg "Что? просто тупик?"
            lea "Давай вернёмся обратно"
            gg "Ну, больше вариантов у нас нет"
            jump CROSS
        label goRight:
            hide leaSad
            show leaDis at right
            lea "Что это?"
            gg "Дерево упало прямо на дорогу"
            hide ggN
            show ggA at left
            lea "Как нам проехать?"
            gg "Придется выйти из машины и дальше пройтись пешком"
            hide leaDis
            hide ggA
            show leaSad at right
            show ggN at left
            lea "Я не думаю, что это хорошая идея"
            menu:
                "Вернуться обратно":
                    jump CROSS
                "Идти пешком":
                    stop music fadeout 1.0
                    play music "audio/forest.mp3" fadein 1.0

                    scene forest
                    show leaSad at right
                    show ggN at left
                    gg "Ладно, идём"
                    hide leaSad
                    show leaSir at right
                    lea "Это дерево так странно выгллядит..."
                    gg "Что ты имеешь в виду?"
                    lea "Ощущение, будто его специально сюда поставили"
                    gg "Звучит как бред, кому это нужно?"
                    gg "Давай просто пойдём дальше, может встретим кого-то"
                    "30 мин спустя"
                    hide leaSir
                    show leaVeryHap at right
                    hide ggN
                    show ggH at left
                    lea "Ты видишь?...Там вроде что-то есть"
                    gg "Да, крыши домов, наконец-то мы нашли хоть что-то"
                    gg "Tам точно должны быть люди, давай найдём кого-то и спросим дорогу"
                    lea "Странное место, оно меня пугает"
                    gg "Ну, другогo выбора у нас нет"
                    ".........."
                    jump Part1
        label goLeft:
            hide ggN
            hide leaSad
            show leaVeryAn at right
            show ggA at left
            gg "Обрыв на краю леса, просто круто"
            lea "Стой, смотри, там вдалеке виднеются какие-то здания"
            hide leaVeryAn
            show leaDis at right
            gg "Ну а как нам по-твоему туда добраться?"
            lea "Давай вернёмся обратно и выберем другой поворот"
            jump CROSS

        label goBack:
            lea "Тебе не кажется, что мы здесь уже были?"
            hide ggN
            show ggA at left
            gg "Разве? Вроде нет"
            lea "Нет, точно были. Я запомнила это дерево"
            gg "Кругом лес, тут все деревья одинаковые"
            lea "Остановись, я оставлю крестик на нём"
            gg "Это шутка?"
            hide leaS
            show leaAngry at right
            lea "Я говорю, останови, и я тебе докажу, что мы тут уже были"
            gg "Хорошо..."

            hide leaAngry
            show leaSad at right
            hide ggA
            show ggN at left
            "Полчаса спустя"

            lea "Воооот. Стой!"
            hide ggN
            show ggA at left
            hide leaSad
            show leaDis
            gg "Что уже случилось, ты хочешь в туалет?"
            lea "Нет, крестик! Вот он. Я же тебе говорила, что мы ездим кругами"
            hide leaDis
            show leaSad at right
            gg "Не может быть..."
            lea "Вернись к перекрёстку"
            jump CROSS

label Part1:
    scene village
    show ggN at left
    show leaSad at right
    gg "Почему-то не видно никого, это странно"
    hide leaSad
    show leaSmile at right
    lea "Я вижу человека в далеке, пошли к нему"
    hide leaSmile

    hide ggN
    show ggH at left
    show celBack at right
    gg "Здравствуйте, мы заблудились, не могли бы вы подсказать нам дорогу"
    "..."
    gg "Эй, вы меня слышите?"
    "..."
    "..."
    "..."
    hide ggH
    show ggA at left

    gg "Что тут вообще происходит, может он глухой?"
    "ты дотрагиваешься до человека рукой"
    stop music fadeout 1.0
    play music "audio/krik.mp3"

    hide celBack
    show celFont at right
    "ААААААААА"
    hide ggA
    show ggScarry at left
    gg "ГОСПОДИ, ЧТО ПРОИСХОДИТ"
    "АААААААА"
    lea "Милый, давай вернёмся"
    "ААААААА"
    gg "Там ещё люди"
    "Вас начинают окружать другие люди"

    hide cell
    hide ggScarry
    show ggScarry at center
    gg "Извините, мы не хотели причинить вред, просто мы заблудились"
    "АААААА"
    gg "Вы можете объяснить что здесь происходит"
    "ААААА"


    gg "Что за чертовщина тут творится"
    gg "Я не понимаю, что с ними не так, Господи, они просто смотрят"
    gg "а этот...он не перестаёт кричать..."
    gg "ЧТО ЧЁРТ ВОЗЬМИ ПРОИСХОДИТ"
    gg "пора сваливать отсюда"
    stop music fadeout 1.0
    play music "audio/dih.mp3" fadein 1.0
    hide celFont
    gg "Давай вернёмся к машине"
    gg "Лея?"
    gg "Чёрт, что... Она же была рядом, куда она делась."
    gg "ГДЕ ЛЕЯ, КУДА ВЫ ЕЁ ДЕЛИ?"
    "АААА"
    gg "это она, с какой стороны крик..."
    gg "я не моу понять..."
    gg "нужно бежать..."
    gg"бежать хоть куда-то"

    menu:
        "Бежать":
            jump RUN
        "Бежать":
            jump RUN
        "Бежать":
            jump RUN
        "Бежать":
            jump RUN
label RUN:
    gg "крик..."
    gg "он не прекращается..."
    gg "моя голова, я не могу.."
    gg "воздуха не хватает, что происходит"
    scene black
    hide ggScarry
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."

    stop music fadeout 1.0
    play music "audio/forest.mp3" fadein 1.0

    scene bedroom
    show leaVeryHap at right
    show ggH at left
    lea "Милый, доброе утро, просыпайся, соня."
    lea"Сегодня твой день."
    gg"Солнце, доброе утро"
    lea"С днём рожления, я тебя очень сильно люблю"
    gg"Спасибо, я тебя тоже люблю"
    lea "Вставай, сегодня будет лучший день"
    gg "Раз сегодня мой день, я решаю еще поваляться"
    lea"хвхвхвв, хорошо, милаш"
    lea "Но только я с тобой "
    gg"А как иначе"
    hide leaVeryHap
    hide ggH
    show leaSmile at right
    show ggN at left
    lea"Как тебе спалось?"
    gg"не очень, снилось что-то дурацое"
    lea"И что же?"
    gg"мы с обой заблудились в лесу и попали в какой-то странный город"
    gg"Хотели спросить дорогу у жителя"
    gg"Но он просто начал кричать"
    gg"А потом ты пропала"
    gg"Не хочу забивать этим голову"
    gg"Это всего лишь сон"
    hide leaSmile
    hide ggN
    show ggH
    gg"Сейчас я хочу самый вкусный кофе от самой красивой дувушки"
    gg"Сделаешь?"
    "..."
    gg"Солнце, чего молчишь?"
    gg"Лея..."
    hide ggH
    show leaD
    "AAAAAAAA"
    stop music fadeout 1.0
    play music "audio/dih.mp3" fadein 1.0

    scene black
    "AAAAAA"
    "ЧТО ЭТО БЫЛО"
    "темно...сыро..холодно"
    "нужно открыть глаза...тяжело"
    "запах...что это"
    "гниль и земля"
    "нужно открыть глаза"
    "где я вообще"
    "нужно открыть глаза"
    "открыть...глаза"
    "голова болит."
    scene inpit
    "так же темно"
    "где я, нужно попытаться встать."
    "пальцы утопают в земле."
    "я вижу небо, зёзды"
    "как прекрасно:"
    "Стоп, я...в яме?"
    "Господи, что происходит"
    gg "ЭЙ! КТО-НИБУДЬ!ПОМОГИТЕ!"
    "ну же, хоть кто-нибудь... я слышу шаги"
    stop music fadeout 1.0
    play music "audio/rain.mp3" fadein 1.0

    show sill at center
    sil "Ты проснулся..."
    gg "Где я, что происходит?!"
    sil "Тебя не должно быть здесь..."
    sil "Но раз уж ты здесь..."
    gg "Что происходит? Помоги мне выбраться!"
    sil "Хорошо"
    hide sill
    gg"ЭЙ стой"
    "куда он ушёл, нет, Господи, пожалуйста"
    gg"ЭЙ, ВЕРНИСЬ, ПОЖАЛУЙСТА"
    show sill at center
    sil"Не кричи, идиот"
    hide sill
    sil"Поднимайся"
    menu:
        "Подняться":
            
            "Руки дрожат, нужно поднятся,..как же холодно"
            "Эта лестница кажется бесконечной, я чувствую воздух, свежий, почти поднялся, руки совсем не слушаются"
            scene pit
            show ggScarryDB
            gg "Что вам от меня нужно?"
            sil "Ответы...А ты...ты, похоже, не знаешь ничего"
            gg "Что ты несёшь?"
            sil "Пошли со мной, скоро ты всё узнаешь"
            menu:
                "Идти с людьми в капюшонах":
                    jump GoWithPeople
                "Убежать от них":
                    jump RunFromPeople

label GoWithPeople:
    show ggScarryDB
    "сердце бешено колотится, выбора всё рано нет, нужно с ними идти"
    "Они меня окружили, один впереди, двое сзади"
    sil"Топай, или хочешь обратно в яму?"
    gg"Чёрт с вами"
    hide ggScarryDB
    show ggCloseEyesDB
    "Ноги подкашиваются от усталости. округ лес."
    "Этот город очень странно расположен, вокруг ничего кроме леса."
    "Одна тропинка."
    "Даже если я попытаюсь убежать, вряд ли уйду далеко."
    gg"Куда вы меня ведёте?"
    hide ggCloseEyesDB
    show ggScarryDB
    sil"Домой"
    gg"Что это значит?"
    "..."
    "молчит."
    "А может это прото сон?"
    "нужно ущепнуть себя..."
    "ай..э"
    "нет ничего не поменялось."
    "Нужно хотя бы запомнить дорогу, если что-то будет, смогу сбежать"
    "Идиот, тут только одна дорога, что запоминать."
    menu:
        "Идти дальше":
            scene villageNight
            show ggScarryDB
            "сколько мы уже идём..."
            "кроме леса я ничего не вижу."
            "Ноги уже не держут я устал, сколько вообще прошло дней."
            "В голове туман, я ничего не помню"
            sil"мы пришли"
            gg"Что? куда?"
            "дом? как он тут появился, я не видел его до этого"
            sil"Заходи"
            gg"Что это за место?"
            sil"Здесь живут такие же как ты"
            gg"Что это значит?"
            sil"заходи..."
            "Почему он мне ничего не говорит, чёрт..."
            gg"Скажи мне хоть что-нибудь"
            sil"Нет"
            gg"А почему тогда я должен вам верить?"
            sil"У тебя нет выбора"
            
            "Крест? Зачем он тут."
            "ещё и под ногами что-то мокрое"
            "мерзость"
            "Господи..."
            "это...это.."
            "КРОВЬ?"
            "Она течёт как ручей прямо к..."
            scene crest
            "кресту"
            "На нем ввисит тело"
            "что за чертовщина"
            "они сатанисты"
            "Господи нужно бежать, срочно бежать"
            sil"Ты думаешь у тебя получится сбежать?"
            "..."
            sil"Она тоже так думала"
            sil"её самоуверенность не привела ни к чему хорошему"
            sil"Так что подумай еще раз"
            gg"Она?"
            gg"Кто она?"
            scene villageNight
            hide ggScarryDB
            show ggCryDB
            sil"..."
            gg"Нет..."
            gg"не может быть это не она"
            gg"точно не она."
            gg"НЕЕЕТ"
            gg"НЕТ НЕТ"
            gg"ЭТО НЕ ОНА "
            gg"НЕ МОЖЕТ БЫТЬ, НЕТ"
            gg"НЕЕЕТ"
            gg"ЭТО НЕ ОНА, НЕ ОНА НЕЕЕТ"
            gg"Это… это не может быть…"
            sil"Ты должен был умереть вместе с ней..."
            sil"Но ты оказался другим."
            sil"Мы дали тебе шанс…"
            gg"Кто… кто это сделал?"
            gg"Я СПРШИВАЮ КТО ЭТО СДЕЛАЛ"
            "..."
            gg"я убью тебя я убью их всех." 
            gg"я выберусь оттсюда и вы заплатите за это"
            gg "aaaaa"
            scene black
            sil"Да-да, отомстишь, убьёшь"
            sil"Удачи"
            sil"Эй ты, тащи его в дом"
            jump part2
label RunFromPeople:
    show ggScarryDB 
    stop music fadeout 1.0
    play music "audio/dih.mp3" fadein 1.0

    "Бежать... нужно ебжать"
    "не важно куда просто бежать"
    "Господи как болит голова."
    "Это ужасно, я не могу...нужно бежать"
    "Я перестаю видеть, всё в тумане..."
    "в голове звенит"
    scene black
    "Нет, нет, Лея точно, где она, я её потерял"
    "..."
    "..."
    "..."    
    sil"Идиот, я же сказал, что бежать некуда"
    sil"Он в отключке"
    sil"Тащи его в дом, там разберёмся"
    jump part2



return
