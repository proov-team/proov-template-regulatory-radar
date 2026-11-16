# findings/

Your agent writes its emitted output here — a `findings.json` in the shape of
[`../data/sample_expected_output.json`](../data/sample_expected_output.json), one object per
detected gap (company · product · regulation · source_url · gap · deadline · severity ·
recommended_action · alert).

Keep this folder **git-tracked** so your emitted findings are part of the submission — the
grader reads them. Commit your findings as they stabilise, not just at the end.
