# Retrieval eval report

- date: 2026-11-07  queries: 50  runtime: 343s
- LLM: nvidia (nvidia/nemotron-3-ultra-550b-a55b), rerank: False
- theme match = equal or substring, no synonyms

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 68% (n=22) | 75% (n=12) | 67% (n=3) | 0% (n=2) | 67% (n=3) | 100% (n=2) |
| theme overlap: rewrite themes | 67% (n=50) | 58% (n=25) | 77% (n=8) | 67% (n=6) | 96% (n=6) | 65% (n=5) |
| theme overlap: retrieved situations' themes | 52% (n=50) | 56% (n=25) | 48% (n=8) | 44% (n=6) | 43% (n=6) | 58% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `arjuna-hesitates-bhishma`, `arjuna-jayadratha-vow-sunset`
- q15 (en): expected `eklavya-drona-thumb`, got `draupadi-disrobing-sabha`, `drona-demands-drupada`
- q24 (en): expected `duryodhana-maya-palace`, got `kunti-reveals-karna`, `bhima-vows-revenge`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-hesitates-bhishma`, `arjuna-jayadratha-vow-sunset`
- q35 (hi): expected `duryodhana-maya-palace`, got `bhima-spares-jayadratha`, `kunti-reveals-karna`
- q38 (hi): expected `draupadi-disrobing-sabha`, got `bhima-vows-revenge`, `kunti-reveals-karna`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `draupadi-disrobing-sabha`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: The person is facing upcoming exams and finds themselves unable to study, experiencing a mental freeze each time they attempt to open a book.
- themes: anxiety, fear of failure, procrastination, stress, exams  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-hesitates-bhishma` 0.0328; `arjuna-jayadratha-vow-sunset` 0.0318
- verses: `13.10` 0.583 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.56` 0.534 [direct] He whose mind is free from anxiety amid pains, indifferent amid pleasu…; `18.9` 0.466 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `aswamedha-17-2` 0.553 [direct]; `santi-216-2` 0.545 [direct]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: The person is struggling with a profound sense of identity loss and grief after their four-year relationship ended, feeling uncertain about who they are without their partner.
- themes: grief, identity loss, heartbreak, loneliness, self-worth  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `yudhishthira-grief-after-victory` 0.0313
- verses: `13.10` 0.647 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `4.40` 0.534 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `6.6` 0.527 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-174-3` 0.568 [direct]; `vana-65-6` 0.548 [situation:nala-damayanti-teaches-patience]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: The person feels torn between their parents' wish for them to become a doctor and their own desire to study music, experiencing a sense of betrayal toward their family.
- themes: family, duty, guilt, career, passion  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0328; `amba-vow-against-bhishma` 0.0318
- verses: `3.35` 0.553 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.62` 0.545 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.520 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-28-4` 0.580 [direct]; `santi-174-3` 0.548 [direct]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: The person is grieving the recent loss of their mother and feels persistent guilt, believing they should have done more for her before she passed away.
- themes: grief, guilt, loss, regret, family  (expected: grief, guilt, loss)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0320; `gandhari-lament-sons` 0.0315
- verses: `2.7` 0.580 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.40` 0.579 [direct] In the destruction of a family the immemorial family traditions perish…; `2.67` 0.562 [direct] Such of the roving senses as the mind yieldeth to, that hurries away t…
- passages: `santi-277-3` 0.573 [direct]; `stri-2-3` 0.563 [direct]

### q05 (en) — HIT

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: The person was publicly shouted at by their manager in front of the whole team, while colleagues remained silent, leaving them feeling humiliated and powerless.
- themes: humiliation, anger, powerlessness, workplace, loneliness  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `bhima-vows-revenge` 0.0320
- verses: `18.25` 0.573 [direct] The action undertaken from delusion, without regard to capacity and co…; `11.40` 0.544 [direct] Prostrate in front of Thee, prostrate behind; Prostrate on every side …; `2.63` 0.533 [direct] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-111-10` 0.568 [direct]; `vana-29-1` 0.523 [direct]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: The person feels bitter and resentful after their best friend received a promotion they had been working hard to obtain.
- themes: envy, friendship, career, bitterness, professional rivalry  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `karna-envy-arjuna-tournament` 0.0323; `duryodhana-maya-palace` 0.0320
- verses: `2.7` 0.590 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `6.6` 0.572 [direct] The Self is the friend of the self of him in whom the self by the Self…; `16.16` 0.503 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-138-14` 0.582 [direct]; `santi-80-3` 0.573 [direct]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: The person has moved to a new city and feels isolated with no one to talk to, finding weekends especially difficult.
- themes: loneliness, isolation, relocation, sadness  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0323; `pandavas-final-journey-renunciation` 0.0315
- verses: `3.2` 0.530 [direct] With these perplexing words Thou only confusest my understanding; ther…; `2.22` 0.528 [direct] As a man, casting off worn-out garments, taketh new ones, so the dwell…; `11.42` 0.519 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…
- passages: `santi-177-5` 0.553 [direct]; `santi-28-4` 0.535 [direct]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: The person lied to their spouse about finances and the deception has escalated to a point where they feel unable to confess or undo it.
- themes: deception, guilt, marriage, trust, fear of consequences  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0323; `dhritarashtra-lac-house` 0.0309
- verses: `16.10` 0.638 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.34` 0.572 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `16.11` 0.567 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-109-3` 0.608 [direct]; `santi-138-14` 0.576 [direct]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: The person lost all their savings through crypto trading and continues to place more bets in a desperate attempt to recover the lost money.
- themes: financial loss, gambling addiction, desperation, compulsion, risk-taking  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `savitri-satyavan` 0.0313
- verses: `16.12` 0.591 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `16.10` 0.589 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.566 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-104-5` 0.571 [direct]; `santi-177-2` 0.550 [direct]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: The person is torn between reporting a friend's unethical behavior at work and staying loyal to the friend who helped them secure the job, feeling conflicted about duty and gratitude.
- themes: loyalty, ethics, workplace, gratitude, moral dilemma  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0325; `kunti-reveals-karna` 0.0313
- verses: `3.35` 0.637 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.604 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `18.47` 0.594 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-80-2` 0.562 [direct]; `santi-138-14` 0.555 [direct]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: The person made a deathbed promise to their father to take over his shop, but they deeply dislike the work and feel it is destroying their well-being.
- themes: duty, family, guilt, resentment, personal fulfillment  (expected: vow, duty, family, career)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0323; `bhima-vows-revenge` 0.0323
- verses: `3.35` 0.656 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.40` 0.567 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.566 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-277-2` 0.594 [direct]; `santi-277-3` 0.591 [direct]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: The person feels betrayed by their brother who took their rightful share of the family property, and they are consumed by a strong desire for revenge.
- themes: betrayal, anger, revenge, family conflict, property dispute  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0328; `amba-vow-against-bhishma` 0.0312
- verses: `2.62` 0.612 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.597 [direct] In the destruction of a family the immemorial family traditions perish…; `2.63` 0.597 [direct] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-259-2` 0.655 [direct]; `santi-104-5` 0.594 [direct]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: The person has just discovered they were adopted and their birth mother wants to meet them, leaving them feeling angry and confused.
- themes: adoption, identity, anger, confusion, family  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `bhima-vows-revenge` 0.0318
- verses: `2.62` 0.548 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.7` 0.519 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `6.42` 0.506 [direct] Or he may even be born into a family of wise Yogîs; but such a birth a…
- passages: `anusasana-49-1` 0.553 [direct]; `santi-266-4` 0.506 [direct]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: The person is being mocked by peers at college for coming from a village and having weak English, leading to feelings of humiliation and social exclusion.
- themes: humiliation, social exclusion, shame, language barrier, identity  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0323; `draupadi-disrobing-sabha` 0.0315
- verses: `2.7` 0.558 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.15` 0.546 [direct] "I am wealthy, well-born; what other is there that is like unto me? I …; `2.34` 0.483 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-107-4` 0.558 [direct]; `anusasana-37-2` 0.519 [direct]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: The person's professor claimed credit for their research and threatened to withhold their degree if they speak out, leaving them feeling trapped, powerless, and afraid for their academic future.
- themes: exploitation, power abuse, academic integrity, fear, helplessness  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `draupadi-disrobing-sabha` 0.0328; `drona-demands-drupada` 0.0313
- verses: `16.10` 0.591 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.589 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.12` 0.536 [situation:drona-demands-drupada] Held in bondage by a hundred ties of expectation, given over to lust a…
- passages: `santi-111-10` 0.598 [direct]; `santi-138-14` 0.555 [direct]

### q16 (en) — HIT

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: The person feels that their parents consistently side with their younger brother even when he is at fault, leading to a sense of unfair treatment and resentment.
- themes: family, favoritism, unfairness, sibling rivalry, resentment  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `kunti-reveals-karna` 0.0328; `dhritarashtra-lac-house` 0.0318
- verses: `13.10` 0.594 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `1.34` 0.580 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.568 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-105-2` 0.612 [direct]; `santi-80-4` 0.610 [direct]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: The person won a lawsuit against their former business partner but feels empty instead of happy. They expected relief or joy but are experiencing a sense of hollowness.
- themes: emptiness, victory, legal battle, business partnership, disillusionment  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0328; `nala-damayanti-teaches-patience` 0.0306
- verses: `15.5` 0.577 [direct] Without pride and delusion, victorious over the vice of attachment, dw…; `9.12` 0.575 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `7.27` 0.478 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `santi-177-5` 0.561 [direct]; `santi-25-3` 0.533 [direct]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: The person struggles with intense anger that leads to hurtful outbursts, and feels deep regret after screaming at their children.
- themes: anger, regret, parenting, guilt, family  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `kunti-reveals-karna` 0.0323
- verses: `2.63` 0.605 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.566 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.557 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-146-3` 0.576 [direct]; `vana-29-1` 0.538 [direct]

### q19 (en) — HIT

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: The person is caring for a husband with a terminal illness, feeling determined to keep fighting despite the medical prognosis, while likely experiencing fear, grief, and hope.
- themes: caregiving, terminal illness, hope, grief, determination  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `nala-damayanti-teaches-patience` 0.0317; `savitri-satyavan` 0.0315
- verses: `13.10` 0.593 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `12.19` 0.580 [direct] Taking equally praise and reproach, silent, wholly content with what c…; `18.45` 0.507 [situation:savitri-satyavan] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `santi-226-4` 0.576 [direct]; `vana-295-11` 0.537 [situation:savitri-satyavan]

### q20 (en) — HIT

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: The person has been unemployed for two years and feels increasingly worthless with each job rejection, yet continues to keep trying.
- themes: unemployment, worthlessness, rejection, perseverance, self-esteem  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `yudhishthira-dice-game` 0.0313; `nala-damayanti-teaches-patience` 0.0312
- verses: `13.10` 0.562 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.34` 0.529 [direct] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `16.15` 0.520 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `sauptika-2-3` 0.597 [direct]; `santi-139-10` 0.555 [direct]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: The person's team leader consistently makes poor decisions, yet they are required to publicly endorse and support those decisions, creating a conflict between their professional obligations and their own judgment.
- themes: workplace, authority, integrity, frustration, loyalty  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `karna-refuses-bhishma-command` 0.0310; `arjuna-kurukshetra-dilemma` 0.0309
- verses: `2.7` 0.588 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `5.15` 0.525 [direct] The Lord accepteth neither the evil-doing nor yet the well-doing of an…; `10.33` 0.513 [direct] Of letters the letter A I am, and the duality of a compound; I also ev…
- passages: `santi-111-10` 0.581 [direct]; `santi-321-11` 0.575 [direct]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: The person is 70 years old with settled children and feels a strong desire to release all attachments and responsibilities, yet experiences fear about doing so.
- themes: aging, fear, letting go, attachment, mortality  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.0320; `kunti-reveals-karna` 0.0305
- verses: `2.62` 0.535 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `3.19` 0.515 [direct] Therefore, without attachment, constantly perform action which is duty…; `5.12` 0.494 [direct] The harmonised man, having abandoned the fruit of action, attaineth to…
- passages: `santi-289-2` 0.588 [direct]; `adi-159-5` 0.582 [direct]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: The person made a firm commitment to their team that deadlines would never be missed, and now finds that honoring this promise is driving the entire team toward exhaustion.
- themes: leadership, burnout, promises, pressure, responsibility  (expected: vow, pride, duty)
- expected situation: -
- situations: `arjuna-jayadratha-vow-sunset` 0.0328; `amba-vow-against-bhishma` 0.0315
- verses: `18.45` 0.591 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `16.10` 0.578 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.9` 0.527 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `anusasana-121-3` 0.537 [direct]; `sauptika-2-1` 0.526 [direct]

### q24 (en) — MISS

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: The person feels overlooked and undervalued because their cousin is constantly compared to them and the family celebrates all of the cousin's achievements.
- themes: comparison, family, favoritism, resentment, self-worth  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `kunti-reveals-karna` 0.0325; `bhima-vows-revenge` 0.0313
- verses: `1.40` 0.586 [direct] In the destruction of a family the immemorial family traditions perish…; `13.10` 0.576 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `6.6` 0.545 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-80-4` 0.634 [direct]; `santi-138-14` 0.563 [direct]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: The person feels uncertain about their life direction and purpose, perceiving that others have clear plans while they do not.
- themes: confusion, purpose, anxiety, comparison, direction  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0320; `amba-vow-against-bhishma` 0.0311
- verses: `13.10` 0.656 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.7` 0.621 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.63` 0.608 [direct] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-104-5` 0.595 [direct]; `santi-25-3` 0.591 [direct]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: The person is facing upcoming board examinations and feels unable to study, fearing they will fail.
- themes: fear of failure, anxiety, academic pressure, helplessness, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-hesitates-bhishma` 0.0323; `arjuna-jayadratha-vow-sunset` 0.0323
- verses: `11.45` 0.563 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `11.23` 0.545 [direct] Thy mighty Form, with many mouths and eyes, Long armed, with thighs an…; `10.4` 0.543 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…
- passages: `santi-138-21` 0.555 [direct]; `santi-226-3` 0.553 [direct]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: The person's father wants them to pursue engineering but their own interest lies in art, leading to daily arguments at home.
- themes: family, career, duty, parental pressure, anger  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0328; `dhritarashtra-lac-house` 0.0318
- verses: `2.62` 0.563 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `3.35` 0.522 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.34` 0.517 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `santi-296-1` 0.557 [direct]; `vana-112-3` 0.541 [direct]

### q28 (hinglish) — HIT

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: The person was publicly humiliated by someone and now feels a strong urge to retaliate.
- themes: humiliation, anger, revenge, public shame, retaliation  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0320
- verses: `16.10` 0.633 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.63` 0.613 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.610 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…
- passages: `santi-300-3` 0.578 [direct]; `santi-111-10` 0.573 [direct]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: The person is unable to sleep since the breakup and finds that memories of their former partner intrude into every aspect of their life.
- themes: grief, heartbreak, insomnia, loneliness, loss  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `aswatthaman-night-massacre` 0.0320; `savitri-satyavan` 0.0318
- verses: `13.10` 0.619 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.63` 0.576 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `6.24` 0.523 [direct] Abandoning without reserve all desires born of the imagination, by the…
- passages: `santi-216-2` 0.585 [direct]; `santi-104-5` 0.541 [direct]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: The person is conflicted because a friend who supported them during difficult times is now doing something wrong, and they are unsure how to respond.
- themes: loyalty, friendship, moral dilemma, gratitude, guilt  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0311; `karna-parashurama-curse-lineage` 0.0306
- verses: `2.7` 0.676 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.621 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `6.6` 0.614 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-138-14` 0.639 [direct]; `sauptika-5-1` 0.589 [direct]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: The person feels left behind as colleagues have advanced further in their careers, and they experience intense jealousy about this situation.
- themes: envy, career, comparison, inadequacy, frustration  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `karna-refuses-bhishma-command` 0.0318; `nala-damayanti-teaches-patience` 0.0315
- verses: `11.33` 0.551 [direct] Therefore stand up! win for thyself renown, Conquer thy foes, enjoy th…; `16.11` 0.548 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `4.22` 0.534 [direct] Content with whatsoever he obtaineth without effort, free from the pai…
- passages: `santi-111-10` 0.589 [direct]; `santi-104-5` 0.561 [direct]

### q32 (hinglish) — HIT

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: The person lied to ensure their sister's marriage could proceed, and now suffers overwhelming guilt over the deception.
- themes: guilt, deception, family duty, moral conflict, sacrifice  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `bhima-vows-revenge` 0.0325; `yudhishthira-ashwatthama-lie` 0.0317
- verses: `3.35` 0.642 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.593 [direct] Better is one's own duty though destitute of merits than the well-exec…; `1.40` 0.591 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-109-3` 0.622 [direct]; `adi-159-4` 0.616 [direct]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: The person experiences intense anger that flares up over minor issues, causing them to shout at everyone around them.
- themes: anger, irritability, emotional outbursts, relationships, self-control  (expected: anger, self-control, regret)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `yudhishthira-dice-game` 0.0308
- verses: `2.62` 0.592 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `13.21` 0.565 [direct] Matter is called the cause of the generation of causes and effects; Sp…; `16.11` 0.547 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-25-3` 0.572 [direct]; `vana-29-1` 0.564 [direct]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: The person has lost their father and feels unable to cope with the grief.
- themes: grief, loss, coping, family, loneliness  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0318
- verses: `1.40` 0.597 [direct] In the destruction of a family the immemorial family traditions perish…; `1.42` 0.569 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `1.34` 0.557 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `santi-25-3` 0.600 [direct]; `vana-65-6` 0.598 [situation:nala-damayanti-teaches-patience]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: The person feels that their brother consistently receives more love and attention, which triggers strong feelings of jealousy toward him.
- themes: jealousy, sibling rivalry, feeling unloved, family dynamics, envy  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `bhima-spares-jayadratha` 0.0325; `kunti-reveals-karna` 0.0317
- verses: `2.62` 0.609 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `17.21` 0.550 [direct] That given with a view to receiving in return, or looking for fruit ag…; `1.34` 0.529 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `santi-332-2` 0.588 [direct]; `santi-321-19` 0.588 [direct]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: The person made a promise that has turned into a binding trap, leaving them feeling ensnared and burdened by their own commitment.
- themes: duty, guilt, obligation, entrapment, regret  (expected: vow, trap, duty)
- expected situation: -
- situations: `arjuna-jayadratha-vow-sunset` 0.0320; `amba-vow-against-bhishma` 0.0315
- verses: `16.10` 0.666 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `3.35` 0.631 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.9` 0.571 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `santi-321-11` 0.562 [direct]; `drona-79-2` 0.442 [situation:arjuna-jayadratha-vow-sunset]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: The person has lost their job and feels uncertain about the future, experiencing intense fear.
- themes: job loss, uncertainty, fear, career anxiety, future anxiety  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `gandhari-lament-sons` 0.0318
- verses: `9.12` 0.613 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.11` 0.566 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `18.25` 0.549 [direct] The action undertaken from delusion, without regard to capacity and co…
- passages: `santi-104-5` 0.551 [direct]; `santi-80-2` 0.528 [direct]

### q38 (hi) — MISS

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: The person feels humiliated because their mother-in-law repeatedly insults them in front of others, and they feel abandoned because their husband remains silent and does not defend them.
- themes: humiliation, family, marriage, resentment, helplessness  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0325; `kunti-reveals-karna` 0.0323
- verses: `1.40` 0.594 [direct] In the destruction of a family the immemorial family traditions perish…; `1.34` 0.573 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `13.10` 0.573 [direct] Unattachment, absence of self-identification with son, wife or home, a…
- passages: `santi-266-4` 0.565 [direct]; `santi-266-5` 0.563 [direct]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: The person is wrestling with whether to forgive someone who caused them deep emotional pain by breaking their heart.
- themes: forgiveness, heartbreak, betrayal, emotional pain, decision-making  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0320; `bhima-kills-duhsasana-drinks-blood` 0.0315
- verses: `2.7` 0.621 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `10.4` 0.540 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `2.34` 0.502 [situation:amba-vow-against-bhishma] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `udyoga-33-7` 0.588 [direct]; `udyoga-33-6` 0.585 [direct]

### q40 (banglish) — HIT

> Amar boss amake shobar shamne opoman korlo

- rewritten: The person was publicly humiliated by their boss in front of colleagues and feels shamed and hurt by the experience.
- themes: humiliation, workplace, shame, anger, powerlessness  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0323; `bhima-vows-revenge` 0.0323
- verses: `18.27` 0.569 [direct] Impassioned, desiring to obtain the fruit of actions, greedy, harmful,…; `2.63` 0.547 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `17.22` 0.541 [direct] That alms given at unfit place and time, and to unworthy persons, disr…
- passages: `santi-111-10` 0.599 [direct]; `santi-114-1` 0.531 [direct]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: The person feels intense fear before an upcoming exam and believes they are incapable of succeeding.
- themes: fear of failure, anxiety, exam, self-doubt, helplessness  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0325; `draupadi-disrobing-sabha` 0.0313
- verses: `4.40` 0.580 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `10.4` 0.569 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `3.43` 0.562 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-219-5` 0.578 [direct]; `aswamedha-17-2` 0.560 [direct]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: The person feels torn between their parents' wish for them to take a stable job and their own strong desire to start a business.
- themes: family expectations, career, autonomy, duty, fear of disappointing parents  (expected: career, family, duty)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0328; `arjuna-hesitates-bhishma` 0.0311
- verses: `2.62` 0.560 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `3.35` 0.548 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `16.11` 0.538 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-332-2` 0.575 [direct]; `santi-177-3` 0.542 [direct]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: The person feels deeply betrayed by a close friend who stabbed them in the back, leaving them confused and uncertain about how to respond or what to do next.
- themes: betrayal, friendship, confusion, hurt, helplessness  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0318; `bhima-kills-duhsasana-drinks-blood` 0.0311
- verses: `2.63` 0.616 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `6.6` 0.610 [direct] The Self is the friend of the self of him in whom the self by the Self…; `2.7` 0.602 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-138-14` 0.617 [direct]; `santi-139-4` 0.592 [direct]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: The person feels deeply lonely and isolated, with no one to talk to or share their thoughts with.
- themes: loneliness, isolation, emotional pain, need for connection  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0323; `pandavas-final-journey-renunciation` 0.0311
- verses: `13.10` 0.648 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `9.12` 0.625 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `8.6` 0.499 [situation:pandavas-final-journey-renunciation] Whosoever at the end abandoneth the body, thinking upon any being, to …
- passages: `santi-25-3` 0.558 [direct]; `santi-28-4` 0.556 [direct]

### q45 (banglish) — HIT

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: The person has become addicted to online gambling and has lost all their money, feeling overwhelmed and helpless.
- themes: addiction, gambling, financial loss, guilt, helplessness  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `yudhishthira-grief-after-victory` 0.0320
- verses: `16.16` 0.643 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.10` 0.627 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.619 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-104-5` 0.576 [direct]; `santi-177-5` 0.549 [direct]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: The person is unable to accept the death of their father and is overwhelmed by grief.
- themes: grief, denial, loss, family, sadness  (expected: grief, loss, death)
- expected situation: -
- situations: `savitri-satyavan` 0.0325; `gandhari-lament-sons` 0.0315
- verses: `9.12` 0.628 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `1.40` 0.625 [direct] In the destruction of a family the immemorial family traditions perish…; `16.16` 0.583 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-25-3` 0.604 [direct]; `vana-295-11` 0.594 [situation:savitri-satyavan]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: The person feels intense anger and jealousy because everyone seems to love their younger brother more than them.
- themes: jealousy, sibling rivalry, anger, neglect, family  (expected: envy, family, favoritism)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0320; `bhima-vows-revenge` 0.0318
- verses: `2.62` 0.619 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.570 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `1.40` 0.547 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-321-19` 0.610 [direct]; `santi-138-15` 0.572 [direct]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: The person knows their grandfather is doing something wrong, yet the entire family remains silent about it.
- themes: family, moral dilemma, silence, respect, frustration  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `silence-of-elders-udyoga` 0.0328; `bhima-spares-jayadratha` 0.0315
- verses: `1.40` 0.561 [direct] In the destruction of a family the immemorial family traditions perish…; `2.29` 0.544 [direct] As marvellous one regardeth him; as marvellous another speaketh thereo…; `1.34` 0.517 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `sauptika-5-1` 0.580 [direct]; `anusasana-105-2` 0.545 [direct]

### q49 (bn) — HIT

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: The person is repeatedly failing in job interviews and feels unable to maintain patience.
- themes: career, failure, frustration, patience, anxiety  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `shalya-karna-charioteer` 0.0320
- verses: `13.10` 0.603 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.7` 0.554 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `16.11` 0.535 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-111-10` 0.568 [direct]; `sauptika-5-1` 0.524 [direct]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: The person acted impulsively in a moment of anger and now feels deep regret over what they did.
- themes: anger, regret, guilt, impulsivity, remorse  (expected: anger, regret, guilt)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0320
- verses: `2.63` 0.647 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.636 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `16.11` 0.563 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-146-3` 0.596 [direct]; `santi-177-5` 0.570 [direct]
