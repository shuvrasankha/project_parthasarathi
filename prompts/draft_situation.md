You are checking and describing one Mahabharata episode for a self-help index.

Episode (proposed): {title}
Parva: {parva}
Characters: {characters}
Intended dilemma: {focus}

Below are excerpts from candidate sections of K. M. Ganguli's translation of this parva, and some
Bhagavad Gita verses (Annie Besant's translation).

Tasks:
1. `sections`: list the candidate sections whose excerpt actually narrates THIS episode. For each,
   copy one exact passage of 8-25 consecutive words from that excerpt as `quote` (verbatim, no
   changes). A section that only mentions the characters is not enough. If no excerpt narrates the
   episode, return [].
2. `dilemma`: 2-3 sentences describing the human dilemma in modern everyday terms, so someone with a
   similar problem today would recognise it. Do not state story facts that are not in the excerpts
   or in the proposal above. No quotes, no advice, no moral judgement.
3. `themes`: 3-6 lowercase theme keywords (e.g. loyalty, grief, envy, humiliation, duty, forgiveness).
4. `related_verses`: 0-3 verse ids from the list below whose teaching speaks to this dilemma. Only
   ids from the list.

Reply with JSON only:
{{"sections": [{{"section": 0, "quote": "..."}}], "dilemma": "...", "themes": [], "related_verses": []}}

Candidate sections:
{excerpts}

Gita verses:
{verses}
