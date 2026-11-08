You are helping build an index of Mahabharata episodes for a self-help guide. Each episode will be
matched against everyday problems people describe (work, family, relationships, study, loss).

Pick exactly one real episode from the Mahabharata (K. M. Ganguli's English translation, 18 parvas)
for each numbered topic below. Rules:
- Only episodes that are actually narrated in the Mahabharata text. No later retellings, TV serials,
  folk versions or invented details. If you are not sure an episode is in the text, pick another.
- Every episode must be different. Spread them across many parvas and characters.
- `parva` must be one of: {parvas}
- `search_terms`: 5-8 names or distinctive words exactly as they would appear in Ganguli's 1880s
  English (he often uses epithets, e.g. "Pritha" for Kunti, "Radheya" or "Suta's son" for Karna,
  "Partha" or "Dhananjaya" for Arjuna, "Krishna" or "Kesava" for Krishna).
- `sections`: your best guess of the Ganguli section numbers inside that parva ([] if unsure).
  These will be checked against the text, so do not pad the list.
- `id`: short kebab-case slug, unique.
- `focus`: one sentence on the human dilemma, in modern everyday terms.

Already chosen for other topics (do not reuse these episodes):
{taken}

Topics:
{topics}

Reply with JSON only: a list of {n} objects with keys
id, topic_number, title, parva, characters, focus, search_terms, sections.
