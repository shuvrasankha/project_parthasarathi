from rag.sources.gita import clean_english, clean_sanskrit, parse_besant, to_iast

# Shaped like a real Besant discourse page: CSS noise, speaker lines, footnote refs, an OCR-broken
# verse number, a verse starting with इति, and the closing colophon.
PAGE = """
<style>.mw-parser-output .wst-center{text-align:center}</style>
<p>SECOND DISCOURSE.</p>
<p>सञ्जय उवाच ।</p>
<p>तं तथा कृपयाऽऽविष्टमश्रुपूर्णाकुलेक्षणम् ।<br/>विषीदन्तमिदं वाक्यमुवाच मधुसूदनः ॥ १ ॥</p>
<p>Sanjaya said:</p>
<p>To him thus with pity overcome, Madhusûdana spake these words: (1)</p>
<p>श्रीभगवानुवाच ।</p>
<p>कुतस्त्वा कश्मलमिदं विषमे समुपस्थितम् ।<br/>अनार्यजुष्टमस्वर्ग्यमकीर्तिकरमर्जुन ॥ २ ॥</p>
<p>The Blessed Lord said:</p>
<p>Whence hath this dejection befallen thee, ignoble<sup class="reference"><a href="#n1">[1]</a></sup>,
heaven-closing, O Arjuna? (2</p>
<p>इति ते ज्ञानमाख्यातं गुह्याद्गुह्यतरं मया ।<br/>विमृश्यैतदशेषेण यथेच्छसि तथा कुरु ॥ ३ ॥</p>
<p>Thus hath wisdom been declared unto thee by Me. (3)</p>
<p>इति श्रीमद्भगवद्गीतासूपनिषत्सु सांख्ययोगो नाम द्वितीयोऽध्यायः ॥२॥</p>
<p>Thus in the glorious Upanishads of the Bhagavad-Gita, the second discourse.</p>
<ol class="references"><li>↑ Literally, un-Aryan.</li></ol>
"""


def test_parse_besant_aligns_on_sanskrit_markers():
    v = parse_besant(PAGE)
    assert sorted(v) == [1, 2, 3]
    assert v[1] == "Sanjaya said: To him thus with pity overcome, Madhusûdana spake these words:"
    assert v[2] == "The Blessed Lord said: Whence hath this dejection befallen thee, ignoble, heaven-closing, O Arjuna?"
    assert v[3] == "Thus hath wisdom been declared unto thee by Me."  # starts with इति but is a verse


def test_parse_besant_rejects_duplicate_markers():
    page = "<p>क ॥ १ ॥</p><p>One. (1)</p><p>ख ॥ १ ॥</p><p>Again. (1)</p>"
    try:
        parse_besant(page)
    except ValueError as e:
        assert "duplicate" in str(e)
    else:
        raise AssertionError("expected ValueError")


def test_clean_english_strips_colophon_and_numbers():
    assert clean_english("They go to the Supreme. (35) Thus in the glorious Upanishads of ...") == "They go to the Supreme."
    assert clean_english("mind. (23") == "mind."


def test_clean_sanskrit_and_iast():
    raw = "धृतराष्ट्र उवाच\n\nधर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः।\n\nमामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय।।1.1।।\n "
    s = clean_sanskrit(raw)
    assert "1.1" not in s and s.count("\n") == 2
    assert to_iast(s).startswith("dhṛtarāṣṭra uvāca\ndharmakṣetre kurukṣetre")
