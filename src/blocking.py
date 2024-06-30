#all markdown block types
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"



def md_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue

        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    blines = block.split("\n")


    if(
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
            ):
        return block_type_heading

    if len(blines) > 1 and blines[0].startswith("```") and blines[-1].startswith("```"):
        return block_type_code
    
    if block.startswith(">"):
        for line in blines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith("* "):
        for line in blines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist

    if block.startswith("- "):
        for line in blines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist

    if block.startswith("1. "):
        idx = 1
        for line in blines:
            if not line.startswith(f"{idx}. "):
                return block_type_paragraph
            idx += 1
        return block_type_olist

    return block_type_paragraph
    











