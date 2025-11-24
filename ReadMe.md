# 🦖 Dino Run Pygame Játék

Ez a projekt a híres Google Chrome böngésző "Dino Run" játékának egy Python implementációja a **Pygame** könyvtár segítségével. A cél, hogy a dínót irányítva elkerüld az akadályokat (kaktuszok és madarak), és minél magasabb pontszámot érj el a folyamatosan gyorsuló játékban.

## 🚀 Főbb Jellemzők

* **Végtelenített Háttér:** A talaj és a felhők folyamatosan mozognak, illúzióját keltve a végtelen futásnak.
* **Dínó Animációk:** A játékos (dínó) képes futni, ugrani és guggolni.
* **Véletlenszerű Akadályok:** Különböző típusú akadályok (kis és nagy kaktuszok, madarak) jelennek meg véletlenszerű sorrendben.
* **Nehézség Növelése:** Minden 100 pont után a játék sebessége növekszik.
* **Ütközés Érzékelés:** Pontos hitbox alapú ütközés-érzékelés.
* **Menürendszer:** Kezdő képernyő és Game Over menü a pontszám kijelzésével.

---

## ⚙️ A Kód Működése

A játék három fő osztályra épül: `Player`, `Cloud` és `Obstacle` (valamint annak leszármazottai: `SmallCactus`, `LargeCactus`, `Bird`).

### 1. `Player` Osztály

* A dínó **állapotát** (`dino_run`, `dino_jump`, `dino_sneak`) kezeli.
* A `step_index` változó segítségével váltogat a futó/guggoló képek között, létrehozva az **animációt**.
* A `jump()` metódus a gravitációt szimulálja a `jump_vel` (ugrási sebesség) folyamatos csökkentésével.
* A `dino_box` a dínó **hitboxát** (téglalap alakú ütközési terület) tárolja.

### 2. `Cloud` Osztály

* Egyszerű háttérelem a vizuális élmény fokozására.
* Véletlenszerű X és Y koordinátán (`random.randint`) jelenik meg a képernyőn kívül.
* Az `update()` mozgatja balra a felhőt a `game_speed` globális változóval megegyező sebességgel. Ha lement a képernyőről, **újrahasznosítja** egy új, véletlenszerű helyre.

### 3. `Obstacle` Osztályok

* A **Parent (`Obstacle`) osztály** tartalmazza az akadályok alapvető viselkedését (mozgás a `game_speed` alapján, hitbox beállítása, eltűnés a képernyőről).
* A **Leszármazott osztályok** beállítják az egyedi **Y pozíciót** és a **képkészletet**.
* A `Bird` osztály felülírja a `draw()` metódust, hogy saját, kétlépéses animációval rendelkezzen.

---

## 🛠️ Szükséges Modulok és Telepítés

A játék futtatásához szükség van a **Pygame** könyvtárra.

### 1. Pygame telepítése

```bash
pip install pygame
```

### 2. Program futtatása

```bash
python main.py
```

## A Játék irányítása

A játék irányítása rendkívül egyszerű. A program első indításánal megjeélenő főmenüben egy billentyű lenyomásával elindul a játék.
A lefelé nyíl segítségével a felhasználó kitérhet a madarak elől, a felfelé nyíl segítségével átugorhatja a kaktuszokat.

## A játék működése

A felhasználó a dínó karakter irányításával minnél több pont elérésére törekszik. Ha a felhasználó hozzáér egy akadályhoz a játék végetér. A menüből a játékos új játékot indíthat bármelyik bellentyűkapcsoló megnyomásával. A játék 100 pontonként 1 egységgel gyorsul, a dinamikus nehézség miatt.

## Figyelem!
A programot a Vizual Studio Code nevű kódszerkesztőben készítettem, a program tesztelése során a VS Code beépített terminálját használtam. A program bezárása után esetleges hibákat adhat a terminál, hiszen az objektumok megsemmisítését a pygame nem kezeli és sajnos nem találtam olyan forrást amely lehetővé tenné a probléma megoldását, a feladatban nem használtam try/catch blokkokat a hibakezelésre, hiszen az program bezárását követő esetleges hibák nem akadályozzák a játék futását. A tesztelés előtt szükséges a Sprite-ok letöltése, illetve fontos, hogy azonos mappába legyenek mint a `main.py` fájl. Továbbá a program futtatásához szükséges a python telepítése is. 