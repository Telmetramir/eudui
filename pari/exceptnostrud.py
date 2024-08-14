def generate_musicbrainz_disc_id(toc_entries):
    total_frames = sum(entry[2] for entry in toc_entries)
    leadout_frame = toc_entries[-1][1] + 150
    disc_id = (total_frames + leadout_frame) % (1 << 32)
    return (disc_id >> 24 & 0xFF, disc_id >> 16 & 0xFF, disc_id >> 8 & 0xFF, disc_id & 0xFF)
