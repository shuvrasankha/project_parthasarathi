# Retrieval eval report

- date: 2026-11-07  set: heldout.yaml  queries: 30  runtime: 149s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 74% (n=27) | 73% (n=15) | 100% (n=3) | 67% (n=3) | 33% (n=3) | 100% (n=3) |
| theme overlap: rewrite themes | 68% (n=30) | 65% (n=15) | 63% (n=5) | 100% (n=4) | 44% (n=3) | 72% (n=3) |
| theme overlap: retrieved situations' themes | 66% (n=30) | 69% (n=15) | 75% (n=5) | 58% (n=4) | 33% (n=3) | 83% (n=3) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- h01 (en): expected `arjuna-kurukshetra-dilemma`, got `arjuna-hesitates-bhishma`, `shalya-karna-charioteer`
- h02 (en): expected `duryodhana-maya-palace`, got `kunti-reveals-karna`, `draupadi-disrobing-sabha`
- h12 (en): expected `dhritarashtra-lac-house`, got `kunti-reveals-karna`, `bhima-spares-jayadratha`
- h13 (en): expected `vidura-truth-dhritarashtra`, got `shalya-karna-charioteer`, `arjuna-hesitates-bhishma`
- h24 (hi): expected `arjuna-kurukshetra-dilemma`, got `arjuna-hesitates-bhishma`, `yudhishthira-dice-game`
- h25 (banglish): expected `duryodhana-maya-palace`, got `nala-damayanti-teaches-patience`, `bhima-spares-jayadratha`
- h27 (banglish): expected `yudhishthira-dice-game`, got `aswatthaman-night-massacre`, `gandhari-lament-sons`

## Per query

### h01 (en) — MISS

> I froze during my job interview and now I'm scared to even apply anywhere again.

- rewritten: The person froze during a job interview and now feels scared to apply for any jobs again.
- themes: fear, anxiety, self-doubt, career, confidence  (expected: fear of failure, career, paralysis)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-hesitates-bhishma` 0.0307; `shalya-karna-charioteer` 0.0306
- verses: `11.45` 0.554 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `2.7` 0.539 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `4.40` 0.516 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…
- passages: `santi-111-10` 0.566 [direct]; `santi-138-14` 0.538 [direct]

### h02 (en) — MISS

> My sister always gets praised at family dinners and nobody even notices what I've achieved.

- rewritten: The person feels overlooked and undervalued because their sister receives praise at family dinners while their own achievements go unnoticed.
- themes: jealousy, insecurity, family, recognition, resentment  (expected: envy, family, favoritism, self-worth)
- expected situation: duryodhana-maya-palace
- situations: `kunti-reveals-karna` 0.0328; `draupadi-disrobing-sabha` 0.0315
- verses: `1.40` 0.565 [direct] In the destruction of a family the immemorial family traditions perish…; `16.10` 0.556 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `12.19` 0.533 [direct] Taking equally praise and reproach, silent, wholly content with what c…
- passages: `anusasana-44-5` 0.551 [direct]; `santi-80-3` 0.540 [direct]

### h03 (en) — HIT

> My coach makes me give up my weekends and my health so his favourite player can shine.

- rewritten: The person feels forced by their coach to sacrifice weekends and personal health so that the coach's favorite player can succeed, causing frustration and stress.
- themes: exploitation, work-life balance, health, frustration, fairness  (expected: exploitation, injustice, sacrifice, mentor)
- expected situation: eklavya-drona-thumb
- situations: `eklavya-drona-thumb` 0.0315; `shalya-karna-charioteer` 0.0310
- verses: `18.27` 0.569 [direct] Impassioned, desiring to obtain the fruit of actions, greedy, harmful,…; `13.21` 0.551 [direct] Matter is called the cause of the generation of causes and effects; Sp…; `2.7` 0.539 [situation:eklavya-drona-thumb] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `sauptika-2-3` 0.564 [direct]; `udyoga-34-2` 0.558 [direct]

### h04 (en) — HIT

> I gambled away the rent money at a card game last night. My family doesn't know yet.

- rewritten: The person gambled away the rent money in a card game and is anxious because their family does not yet know.
- themes: guilt, financial stress, fear of discovery, family, anxiety  (expected: addiction, gambling, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `kunti-reveals-karna` 0.0318
- verses: `1.40` 0.563 [direct] In the destruction of a family the immemorial family traditions perish…; `2.67` 0.526 [direct] Such of the roving senses as the mind yieldeth to, that hurries away t…; `16.15` 0.522 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `adi-162-2` 0.549 [direct]; `udyoga-37-3` 0.530 [direct]

### h05 (en) — HIT

> My son died in an accident last year. People tell me to move on but I can't.

- rewritten: The person lost their son in an accident last year and feels unable to move on despite others urging them to.
- themes: grief, loss, mourning, depression, helplessness  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `13.10` 0.600 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.16` 0.543 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `18.25` 0.530 [direct] The action undertaken from delusion, without regard to capacity and co…
- passages: `santi-25-3` 0.593 [direct]; `santi-139-8` 0.573 [direct]

### h06 (en) — HIT

> In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.

- rewritten: The person feels humiliated and isolated after being mocked by a colleague in a meeting, with senior people laughing and no one defending them.
- themes: humiliation, embarrassment, loneliness, lack of support, workplace bullying  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0320; `draupadi-disrobing-sabha` 0.0318
- verses: `12.18` 0.569 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `11.42` 0.528 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…; `2.34` 0.501 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-111-10` 0.592 [direct]; `santi-107-4` 0.565 [direct]

### h07 (en) — HIT

> Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.

- rewritten: The person feels torn between their reputation for honesty and the pressure to distort the truth in order to protect their team.
- themes: honesty, integrity, duty, conflict, loyalty  (expected: truth, deception, duty, integrity)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.0328; `vidura-truth-dhritarashtra` 0.0320
- verses: `3.35` 0.602 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.31` 0.573 [situation:vidura-truth-dhritarashtra] That by which one understandeth away Right and Wrong and also what oug…; `18.45` 0.549 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `santi-138-14` 0.592 [direct]; `santi-162-1` 0.574 [direct]

### h08 (en) — HIT

> I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.

- rewritten: The person made a public promise to finish a project by Friday or resign, but it is now Thursday and they are far from completing it.
- themes: commitment, fear of failure, career, anxiety, pressure  (expected: vow, fear of failure, pride)
- expected situation: arjuna-jayadratha-vow-sunset
- situations: `arjuna-jayadratha-vow-sunset` 0.0328; `amba-vow-against-bhishma` 0.0323
- verses: `3.35` 0.559 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.550 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `18.9` 0.507 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `santi-321-11` 0.525 [direct]; `santi-111-10` 0.522 [direct]

### h09 (en) — HIT

> I tried everything to stop two departments from fighting, but nobody would compromise.

- rewritten: The person has tried everything to stop two departments from fighting, but nobody would compromise.
- themes: conflict, compromise, workplace, frustration, leadership  (expected: peace, conflict, mediation, failure)
- expected situation: krishna-peace-mission
- situations: `krishna-peace-mission` 0.0315; `arjuna-hesitates-bhishma` 0.0315
- verses: `18.45` 0.559 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `3.34` 0.532 [direct] Affection and aversion for the objects of sense abide in the senses; l…; `2.18` 0.522 [direct] These bodies of the embodied One, who is eternal, indestructible and i…
- passages: `santi-227-4` 0.546 [direct]; `santi-102-3` 0.538 [direct]

### h10 (en) — HIT

> I finally beat my rival for the top job and now I can't sleep thinking about what it cost.

- rewritten: The person has secured the top job by defeating a rival but now feels unable to sleep, haunted by thoughts about the personal cost and sacrifices involved.
- themes: guilt, anxiety, ambition, competition, remorse  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0323; `arjuna-jayadratha-vow-sunset` 0.0306
- verses: `16.10` 0.623 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.611 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `3.30` 0.554 [direct] Surrendering all actions to Me, with thy thoughts resting on the supre…
- passages: `santi-100-5` 0.595 [direct]; `aswamedha-31-2` 0.595 [direct]

### h11 (en) — HIT

> I just found out the man who raised me isn't my real father. I don't know where I belong.

- rewritten: The person has just discovered that the man who raised them is not their biological father and feels uncertain about where they belong.
- themes: identity, belonging, family, confusion, betrayal  (expected: identity, family, abandonment)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `amba-vow-against-bhishma` 0.0315
- verses: `2.7` 0.555 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.41` 0.525 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…; `1.40` 0.522 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-266-5` 0.566 [direct]; `anusasana-105-2` 0.525 [direct]

### h12 (en) — MISS

> My father always covers for my brother's mistakes, even when they hurt me.

- rewritten: The person feels hurt because their father consistently shields their brother's mistakes, even when those mistakes cause the person pain.
- themes: family, favoritism, resentment, injustice, sibling rivalry  (expected: favoritism, family, injustice)
- expected situation: dhritarashtra-lac-house
- situations: `kunti-reveals-karna` 0.0328; `bhima-spares-jayadratha` 0.0311
- verses: `2.7` 0.574 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.40` 0.571 [direct] In the destruction of a family the immemorial family traditions perish…; `1.34` 0.558 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `anusasana-105-2` 0.598 [direct]; `santi-138-15` 0.577 [direct]

### h13 (en) — MISS

> I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?

- rewritten: The person feels uneasy because they repeatedly warn their boss that a plan will fail, but the boss ignores them, and they are uncertain whether to continue issuing warnings.
- themes: responsibility, fear of failure, workplace conflict, anxiety, authority  (expected: truth, loyalty, duty, counsel)
- expected situation: vidura-truth-dhritarashtra
- situations: `shalya-karna-charioteer` 0.0318; `arjuna-hesitates-bhishma` 0.0317
- verses: `2.7` 0.562 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.553 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.56` 0.448 [direct] He whose mind is free from anxiety amid pains, indifferent amid pleasu…
- passages: `santi-138-21` 0.579 [direct]; `santi-140-5` 0.551 [direct]

### h14 (en) — HIT

> After the layoffs I lost everything, and it has been three years of struggle.

- rewritten: The person lost everything after layoffs and has been struggling for three years.
- themes: loss, unemployment, financial hardship, struggle, hopelessness  (expected: patience, setback, loss, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0325; `yudhishthira-dice-game` 0.0320
- verses: `9.12` 0.608 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.21` 0.542 [direct] Triple is the gate of this hell, destructive of the self—lust, wrath, …; `18.25` 0.530 [direct] The action undertaken from delusion, without regard to capacity and co…
- passages: `santi-104-5` 0.564 [direct]; `santi-299-3` 0.553 [direct]

### h15 (en) — HIT

> Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.

- rewritten: The person feels humiliated after someone insulted his wife, swore to make the person pay, and now the desire for revenge is consuming him.
- themes: humiliation, anger, revenge, guilt, obsession  (expected: revenge, humiliation, anger, vow)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `amba-vow-against-bhishma` 0.0320
- verses: `2.62` 0.650 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.633 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.34` 0.576 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-296-1` 0.596 [direct]; `santi-104-5` 0.565 [direct]

### h16 (hinglish) 

> Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon

- rewritten: The person got nervous during an interview and now feels they are not capable of any work.
- themes: anxiety, self-doubt, insecurity, career, low self-esteem  (expected: fear of failure, self-worth, career)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0311; `draupadi-disrobing-sabha` 0.0306
- verses: `9.12` 0.588 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `2.7` 0.563 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `4.40` 0.535 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…
- passages: `santi-321-19` 0.537 [direct]; `aswamedha-31-2` 0.529 [direct]

### h17 (hinglish) — HIT

> Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai

- rewritten: The person feels jealous because everyone respects their older sister more, and this creates an inner sense of envy. They experience discomfort and comparison with their sibling.
- themes: jealousy, envy, sibling rivalry, insecurity, comparison  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `duryodhana-maya-palace` 0.0308; `kunti-reveals-karna` 0.0306
- verses: `2.62` 0.573 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `3.42` 0.533 [direct] It is said that the senses are great; greater than the senses is the m…; `3.34` 0.524 [direct] Affection and aversion for the objects of sense abide in the senses; l…
- passages: `santi-25-3` 0.592 [direct]; `santi-138-14` 0.592 [direct]

### h18 (hinglish) 

> Papa ki death ke baad sab khaali khaali lagta hai

- rewritten: The person feels a deep sense of emptiness after their father's death, finding everything around them seems hollow and lacking purpose.
- themes: grief, loss, emptiness, loneliness, sadness  (expected: grief, loss, emptiness)
- expected situation: -
- situations: `yudhishthira-grief-after-victory` 0.0320; `gandhari-lament-sons` 0.0315
- verses: `9.12` 0.645 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.11` 0.592 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `13.9` 0.570 [direct] Dispassion towards the objects of the senses, and also absence of egoi…
- passages: `santi-175-3` 0.576 [direct]; `santi-139-8` 0.572 [direct]

### h19 (hinglish) — HIT

> Satta mein saare paise haar gaya, ghar walon ko kaise bataun

- rewritten: The person lost all their money in gambling and wonders how to tell their family.
- themes: loss, guilt, fear, family, shame  (expected: gambling, addiction, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `bhima-vows-revenge` 0.0315
- verses: `1.40` 0.586 [direct] In the destruction of a family the immemorial family traditions perish…; `16.15` 0.572 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …; `16.16` 0.570 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `adi-162-2` 0.585 [direct]; `udyoga-37-3` 0.571 [direct]

### h20 (hinglish) — HIT

> Sabke saamne meri beizzati hui aur koi kuch nahi bola

- rewritten: The person was publicly humiliated and feels that no one spoke up or offered any support.
- themes: humiliation, embarrassment, isolation, loneliness, neglect  (expected: humiliation, silence, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0323; `draupadi-disrobing-sabha` 0.0320
- verses: `12.18` 0.610 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `11.42` 0.553 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…; `2.29` 0.540 [direct] As marvellous one regardeth him; as marvellous another speaketh thereo…
- passages: `santi-111-10` 0.548 [direct]; `santi-80-4` 0.545 [direct]

### h21 (hi) — HIT

> मेरे बेटे की मौत के बाद जीने का मन नहीं करता

- rewritten: The person feels a lack of desire to live after the death of their son.
- themes: grief, depression, loss, hopelessness, family  (expected: grief, loss, despair)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0325; `savitri-satyavan` 0.0318
- verses: `1.40` 0.606 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.591 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `16.16` 0.556 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-174-3` 0.614 [direct]; `vana-295-11` 0.560 [situation:savitri-satyavan]

### h22 (hi) — HIT

> मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है

- rewritten: The person discovered they were adopted in childhood and now feels a strong desire to meet their biological mother, creating emotional conflict about identity and family ties.
- themes: identity, family, belonging, longing, abandonment  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `amba-vow-against-bhishma` 0.0310
- verses: `2.62` 0.586 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `18.24` 0.564 [direct] But that action that is done by one longing for desires, or again with…; `1.40` 0.522 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-174-3` 0.571 [direct]; `santi-104-5` 0.537 [direct]

### h23 (hi) 

> मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?

- rewritten: The person is conflicted because their friend is on a wrong path, yet the friend has always supported them, and they are unsure how to respond.
- themes: loyalty, friendship, moral dilemma, guidance, duty  (expected: loyalty, friendship, duty)
- expected situation: -
- situations: `arjuna-hesitates-bhishma` 0.0318; `karna-parashurama-curse-lineage` 0.0318
- verses: `2.7` 0.666 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.619 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.540 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-138-14` 0.620 [direct]; `santi-80-2` 0.595 [direct]

### h24 (hi) — MISS

> परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ

- rewritten: The person experiences trembling hands and feet before an exam and feels that they forget everything.
- themes: anxiety, fear, exam, stress, self-doubt  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-hesitates-bhishma` 0.0323; `yudhishthira-dice-game` 0.0320
- verses: `13.10` 0.568 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.11` 0.540 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `10.4` 0.536 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…
- passages: `santi-194-2` 0.545 [direct]; `aswamedha-43-3` 0.541 [direct]

### h25 (banglish) — MISS

> Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy

- rewritten: The person feels intense jealousy because everyone loves their sister more than them, and they are struggling with feelings of envy and inadequacy.
- themes: jealousy, envy, sibling, insecurity, inadequacy  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `nala-damayanti-teaches-patience` 0.0313; `bhima-spares-jayadratha` 0.0309
- verses: `16.10` 0.618 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.553 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `15.11` 0.482 [direct] Yogîs also, struggling, perceive Him, established in the Self; but tho…
- passages: `santi-25-3` 0.597 [direct]; `santi-104-5` 0.585 [direct]

### h26 (banglish) — HIT

> Chele mara jawar por ami r kichu bhabte parchi na

- rewritten: The person feels unable to think about anything after the death of their son.
- themes: grief, loss, sadness, helplessness, trauma  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0325; `yudhishthira-grief-after-victory` 0.0325
- verses: `13.10` 0.633 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.11` 0.585 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `16.16` 0.544 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-174-3` 0.588 [direct]; `santi-139-8` 0.580 [direct]

### h27 (banglish) — MISS

> Juar nesha amar sansar sesh kore dicche

- rewritten: The person feels that their world is ending or being destroyed, experiencing overwhelming distress and a sense of hopelessness.
- themes: despair, hopelessness, grief, anxiety, loss  (expected: addiction, gambling, family)
- expected situation: yudhishthira-dice-game
- situations: `aswatthaman-night-massacre` 0.0323; `gandhari-lament-sons` 0.0318
- verses: `9.12` 0.728 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.11` 0.666 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `2.63` 0.656 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-104-5` 0.639 [direct]; `santi-25-3` 0.628 [direct]

### h28 (bn) — HIT

> অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না

- rewritten: The person was publicly humiliated at work in front of everyone and feels isolated because no one defended or spoke up for them.
- themes: humiliation, loneliness, embarrassment, workplace, isolation  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0320; `bhima-vows-revenge` 0.0320
- verses: `18.25` 0.590 [direct] The action undertaken from delusion, without regard to capacity and co…; `11.42` 0.535 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…; `2.34` 0.478 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-111-10` 0.584 [direct]; `santi-80-4` 0.547 [direct]

### h29 (bn) — HIT

> বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না

- rewritten: The person has been searching for a job for many years without success, yet feels unable to stop trying.
- themes: unemployment, frustration, perseverance, anxiety, hopelessness  (expected: patience, setback, perseverance, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0325; `krishna-peace-mission` 0.0310
- verses: `13.10` 0.634 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `18.22` 0.546 [direct] While that which clingeth to each one thing as if it were the whole, w…; `4.22` 0.541 [direct] Content with whatsoever he obtaineth without effort, free from the pai…
- passages: `sauptika-2-3` 0.587 [direct]; `santi-139-10` 0.565 [direct]

### h30 (bn) — HIT

> আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল

- rewritten: The person has learned that their biological mother abandoned them in early childhood and feels hurt, confused, and uncertain about their identity.
- themes: abandonment, identity, grief, loneliness, betrayal  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `aswatthaman-night-massacre` 0.0310
- verses: `13.10` 0.639 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.7` 0.567 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.63` 0.550 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-304-2` 0.582 [direct]; `santi-104-5` 0.538 [direct]
