# anki-ipa-generator
Automatically generates IPA pronunciations for English vocabulary CSV files to create ready-to-import Anki flashcards.

## About The Project

**Anki IPA Generator** is a quick, automated tool built for language learners and Anki users who want to enhance their vocabulary decks with accurate pronunciation guides. 

Instead of manually looking up and entering phonetic symbols for every vocabulary entry, this tool reads your raw English word list from a CSV file, generates International Phonetic Alphabet (IPA) transcriptions using `eng_to_ipa`, and outputs a formatted CSV file tailored for seamless Anki deck imports.

### Key Features
* **Automated IPA Conversion:** Quickly translates English words into standardized IPA phonetic transcriptions.
* **Batch Processing:** Handles large vocabulary lists stored in CSV format using `pandas`.
* **Anki Integration:** Produces structured CSV outputs ready for direct import into custom Anki card templates.