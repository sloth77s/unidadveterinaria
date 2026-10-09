import re
files = [
    'servicios/cardiologia-veterinaria.html',
    'servicios/citopatologia-veterinaria.html',
    'servicios/dermatologia-veterinaria.html',
    'servicios/gastroenterologia-veterinaria.html',
    'servicios/medicina-interna-veterinaria.html',
    'servicios/nefrologia-veterinaria.html',
    'servicios/neurologia-veterinaria.html',
    'servicios/oncologia-veterinaria.html',
    'servicios/ortopedia-veterinaria.html',
    'servicios/radiologia-veterinaria.html',

]–or file in files:
    with open(file, encoding="utf-8") as f:
        c = f.read()
        img = [(m.start(), m.end()) x™½È´¥¸É”¹™¥¹‘¥Ñ•È¡Èˆñ¥µmxùt¨øˆ°Œ¥t(€€€€€€€ÁÉ¥¹Ğ œœ¤¹•Ü±¥¹”(€€€€€€€ÁÉ¥¹Ğ !Pœ°™¥±”¤(€€€€€€€¥µœ€ôl¡´¹ÍÑ…ÉĞ ¤°´¹•¹ ¤¤™½È´¥¸É”¹™¥¹‘¥Ñ•È¡Èˆñ¥µmyyt¨øˆ°Œ¥t(€€€€€€€™½È´¥¸É”¹™¥¹‘¥Ñ•È¡Èˆ¡İ¥‘Ñ¡ñ¡•¥¡Ğ¥qqqÌ¨õqqqmqq‘tˆ°Œ¤è(€€€€€€€€€€€¥¹Í¥‘•}¥µœ€ô…¹ä¡Ì€ğô´¹ÍÑ…ÉĞ ¤€ğ”™½ÈÌ°”¥¸¥µœ¤(€€€€€€€€€€€¥˜¹½Ğ¥¹Í¥‘•}¥µœè(€€€€€€€€€€€€€€€ÁÉ¥¹Ğ ]I9%9èœ™¥±”°€İ¥‘Ñ ½¡•¥¡Ğ¥¸QaP…Ğœ°´¹ÍÑ…ÉĞ ¤°m…à À±´¹ÍÑ…ÉĞ ¤´ĞÀ¤é´¹•¹ ¤¬ĞÁt¤(€€€€€€€™½È´¥¸É”¹™¥¹‘¥Ñ•È¡È‰qqqÉqq¸ˆ°Œ¤è(€€€€€€€€€€€ÁÉ¥¹Ğ ]I9%9è€œ™¥±”°€I1…Ğœ°´¹ÍÑ…ÉĞ ¤°mµ…à À±´¹ÍÑ…ÉĞ ¤´ÌÀ¤é´¹•¹ ¤¬ÌÁt¤(€€€€€€€™½È´¥¸É”¹™¥¹‘¥Ñ•È¡È‰mqpÉàÈµqpÉàÍumqqààÀµqqá‰™tˆ°Œ¤è(€€€€€€€€€€€ÁÉ¥¹Ğ ]I9%9èœ™¥±”°€5=)%	A…Ğœ°´¹ÍÑ…ÉĞ ¤°m…à À±´¹ÍÑ…ÉĞ ¤´ÈÀ¤é´¹•¹ ¤¬ÈÁt¤