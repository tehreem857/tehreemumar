with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The bad section starts right after '<!-- END Robot -->\n\n'
# and ends just before '<!-- Project 1: AI Resume Builder -->'
# We want to replace the entire middle with the correct showcase-label

END_MARKER = '<!-- END Robot -->\n\n'
PROJECT1_MARKER = '<!-- Project 1: AI Resume Builder -->'

idx_end_robot = content.find(END_MARKER)
idx_project1  = content.find(PROJECT1_MARKER)

if idx_end_robot == -1 or idx_project1 == -1:
    print("Markers not found!")
    print("END Robot found:", idx_end_robot != -1)
    print("Project1 found:", idx_project1 != -1)
else:
    # The section between end of END_MARKER and start of PROJECT1_MARKER is the junk
    junk_start = idx_end_robot + len(END_MARKER)
    junk_end   = idx_project1
    print(f"Junk block: chars {junk_start} to {junk_end}, length {junk_end - junk_start}")
    print("First 300 chars of junk:")
    print(repr(content[junk_start:junk_start+300]))

    # Replace the junk with the correct showcase-label div
    clean_label = """          <div class="showcase-label">
            <span class="showcase-dot"></span> Featured Systems &amp; Deployed Work
          </div>

          """

    new_content = content[:junk_start] + clean_label + content[junk_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("DONE - file cleaned!")
    print("New showcase-label count:", new_content.count('showcase-label'))
