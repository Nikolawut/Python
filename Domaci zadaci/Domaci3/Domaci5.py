def worst_p(podcasts):
    worst_ratio = float('inf')
    worst_name = None
    for podcast in podcasts:
        p_comments = podcast['br_pozitivni']
        n_comments = podcast['br_negativni']
        if n_comments != 0:
            ratio = p_comments / n_comments
            if ratio < worst_ratio:
                worst_ratio = ratio
                worst_name = podcast['naziv']
    return worst_name

podcasts = [
    {'naziv': 'Español para principiantesz', 'br_pozitivni': 1000, 'br_negativni': 10},
    {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30},
    {'naziv': 'Science VS.', 'br_pozitivni': 600, 'br_negativni': 45}
]
print("Najgori podcast:", worst_p(podcasts))