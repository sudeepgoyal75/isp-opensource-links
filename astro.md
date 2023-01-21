# Planet speed

- https://www.theplanetstoday.com/hindu_astrology.html
- https://www.quora.com/What-do-the-minutes-mean-on-an-astrology-chart
- https://www.astro.com/swisseph/swepha_e.htm


# info

```
In Astrology we have 9 planets ,12 signs/Rashis and 27stars to predict future.

12 Rashis from Aries to Pisces occupies in 12 houses/bhavas in zodiac.

Each sign is 30 degree. Total 12*30=360°

1° (degree) means 60′ (minutes)

1′(minute) means 60′’ (seconds)

Each star has 4 padas. 27(stars)×4=108 padas

108÷12(signs)=9(Each sign has 9padas)

Each star is 13°20′

Each padam is 3°20′

For example the native born in cancer Ascendant 6°12′24′’ means lagna started at that particular degree minute second in cancer sign.

Moon is in 25°10′11′’ in Aries sign means the native born in Bharani star and star lord venus.
```

yml

```
config:
  rashi:
    vrishabha: 
      seq: 1
      governedby: shukr
      english: tauruis
    mesh:
      seq: 1
      governedby: mangal
      english: aries
    meen:
      seq: 3
      governedby: guru
      english: pisces
    kumbh:
      seq: 4
      governedby: shani
      english: aquarius
    makar:
      seq: 5
      governedby: shani
      english: capricorn
    dhanu:
      seq: 6
      governedby: guru
      english: sagittarius
    vrshchik:
      seq: 7
      governedby: mangal
      english: scorpio
    tula:
      seq: 8
      governedby: shukr
      english: libra
    kanya:
      seq: 9
      governedby: budh
      english: virgo
    simha:
      seq: 10
      governedby: surya
      english: leo
    karka:
      seq: 11
      governedby: chaand
      english: cancer
    kumbh:
      seq: 12
      governedby: budh
      english: gemeni

  planets:
    surya:
      cycle: 365d
      english: sun
      uuch:
        - mesh
      durbal:
        - tula
      friend:
        - moon
        - mars
        - jupiter
      enemy:
        - saturn
        - venus    
  
    chaand:
      cycle: 90m
      english: moon
      uuch:
        - vrishabha
      durbal:
        - vrshchik
      governedby: shukr
      friend:
        - sun
        - murcury
      enemy:

    mangal:
      cycle: 687d
      english: mars
      uuch:
        - makar
      durbal:
        - karka
      governedby: shukr
      friend:
        - sun
        - moon
        - jupitor
      enemy:
        - moon


    budh: 
      cycle: 116d
      english: mercury
      uuch:
        - kanya
      durbal:
        - meen
      friend:
        - sun
        - venus
      enemy:
        - moon

    guru: 
      cycle: 4330.6d
      english: jupitor
      uuch:
        - karka
      durbal:
        - makar
      friend:
        - sun
        - moon
        - mars
      enemy:
        - venus
        - mercury

    shukr: 
      cycle: 243d
      english: venus
      uuch:
        - tula
      durbal:
        - mesh
      friend:
        - saturn
        - mercury
      enemy:
        - all

    shani: 
      cycle: 10756d
      english: saturn
      uuch:
        - tula
      durbal:
        - mesh
      friend:
        - venus
        - mercury
      enemy:
        - all

    rahu: 
      cycle: 6585.3211d
      english: north_node
      uuch:
        - dhanu
      durbal:
        - kumbh
      friend:
        - venus
        - saturn
      enemy:
        - sun
        - moon
        - mars

    ketu: 6585.3211d
      cycle: 116d
      english: mars
      uuch:
        - kumbh
      durbal:
        - dhanu
      friend:
        - venus
        - saturn
      enemy:
        - sun
        - moon
        - mars

  benefit_planet:
    - chaand
    - budh
    - shukr
    - guru
  malefic_planet:
    - surya
    - mangal
    - shani
    - ketu

  translation:
    surya: sun
    chaand: moon
    mangal: mars
    budh: mercury
    guru: jupitor
    brihaspati: jupitor
    shukr: venus
    shani: saturn
    rahu: north_node
    ketu: south_node
    mesh: aries
    vrishabha: tauruis
    meen: pisces
    kumbh: aquarius
    makar: capricorn
    dhanu: sagittarius
    vrshchik: scorpio
    tula: libra
    kanya: virgo
    simha: leo
    karka: cancer
    kumbh: gemeni
```
