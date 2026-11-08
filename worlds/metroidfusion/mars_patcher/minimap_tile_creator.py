from enum import Enum

from mars_patcher.constants.minimap_tiles import ColoredDoor, Content, Edge, MapTile, TileEdges

# Used for the edges of tiles, also used for boss icons that are always visible
COLOR_WHITE_OUTLINE = 1
# Used for normal connections between tiles, this appears as a wall when the
# tile is unexplored. Also used for boss icons that disappear when explored
COLOR_CONNECTION_BG = 2
# Used for the background of tiles, either gray (unexplored), pink (normal),
# or green (hidden)
COLOR_BG = 3
# Used for the outline of blank tiles or tiles that don't fill in the whole square
COLOR_BLANK_OUTLINE = 4
# Used for the background of blank tiles or tiles that don't fill in the whole square
COLOR_BLANK_BG = 5
# Used for the white circle/dot representing items, this hides the item when
# the tile is unexplored
COLOR_WHITE_ITEM = 6
# Used for tiles with a letter in them (navigation, save, etc.)
COLOR_YELLOW_LETTER = 7

# Used for colored pixels on the edge of tiles, including hatches and the
# outline of tiles with letters. These appear white when the tile is unexplored
COLOR_BLUE_EDGE = 8
COLOR_GREEN_EDGE = 9
COLOR_RED_EDGE = 10
COLOR_YELLOW_EDGE = 11

COLOR_COUNT = 4

# Used for colored pixels not on the edge of tiles, including hatches and
# various icons. These are hidden (gray) when the tile is unexplored
COLOR_BLUE_HIDDEN = COLOR_BLUE_EDGE + COLOR_COUNT
COLOR_GREEN_HIDDEN = COLOR_GREEN_EDGE + COLOR_COUNT
COLOR_RED_HIDDEN = COLOR_RED_EDGE + COLOR_COUNT
COLOR_YELLOW_HIDDEN = COLOR_YELLOW_EDGE + COLOR_COUNT

# The following string lists represent pixels in a minimap tile
# - Pixels with "." are left unchanged
# - Pixels with "-" are set to the background color (COLOR_BG)
# - Pixels with "#" are set to a provided color (see draw_pixel_art below)
# - Spaces are ignored

PIXELS_ITEM = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . . # # . . .",
    ". . # . . # . .",
    ". . # . . # . .",
    ". . . # # . . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_NAVIGATION = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . # . . # . .",
    ". . # # . # . .",
    ". . # . # # . .",
    ". . # . . # . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_SAVE = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . . # # # . .",
    ". . # . . . . .",
    ". . . # # . . .",
    ". . . . . # . .",
    ". . # # # . . .",
    ". . . . . . . .",
]
PIXELS_RECHARGE = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . # # # . . .",
    ". . # . . # . .",
    ". . # # # . . .",
    ". . # . . # . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_DATA = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . # # # . . .",
    ". . # . . # . .",
    ". . # . . # . .",
    ". . # # # . . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_SECURITY = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". . # . # . . .",
    ". . # # . . . .",
    ". . # . # . . .",
    ". . # . # . . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_AUXILIARY = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". - # . # . . .",
    ". - . # . . . .",
    ". - # . # . . .",
    ". - # . # . . .",
    ". . . . . . . .",
    ". . . . . . . .",
]
PIXELS_MAP = [
    ". . . . . . . .",
    ". . . . . . . .",
    ". # . . . # . .",
    ". # # . # # . .",
    ". # . # . # . .",
    ". # . . . # . .",
    ". . . . . . . .",
    ". . . . . . . .",
]

PIXELS_BOSS = [
    ". # . . # .",
    ". # # # # .",
    "# # # # # #",
    "# . # # . #",
    ". # # # # .",
    ". # . . # .",
]

# The following string lists represent pixels in a minimap tile
# - Pixels with "." are left unchanged
# - Pixels with "-" are set to the background color (COLOR_BG)
# - Pixels with a hex character (0-9 and A-F) are set to that color
#   (see draw_colored_pixel_art below)
# - Spaces are ignored

COLORED_PIXELS_TUNNEL = [
    "4 4 4 4 4 4 4 4",
    "4 5 5 5 1 5 5 4",
    "1 1 1 5 1 1 5 4",
    "5 5 5 5 1 1 1 4",
    "5 5 5 5 1 1 5 4",
    "1 1 1 5 1 5 5 4",
    "4 5 5 5 5 5 5 4",
    "4 4 4 4 4 4 4 4",
]

COLORED_PIXELS_MAJOR = [
    ". . . . . . . .",
    ". . . 6 6 . . .",
    ". - 6 C C 6 - .",
    ". 6 C 6 C C 6 .",
    ". 6 C C C C 6 .",
    ". - 6 C C 6 - .",
    ". . . 6 6 . . .",
    ". . . . . . . .",
]
COLORED_PIXELS_CHOZO = [
    ". . . . . . . .",
    ". . 6 6 6 . . .",
    ". 6 E E E 6 - .",
    ". E E 6 E E 6 .",
    ". E E E E E 6 .",
    ". E 6 E E E 6 .",
    ". 6 6 E E E 6 .",
    ". . . . . . . .",
]

HAS_RED_OUTLINE = {
    Content.EMPTY_RED_WALLS,
    Content.NAVIGATION,
    Content.SAVE,
    Content.RECHARGE,
    Content.HIDDEN_RECHARGE,
    Content.DATA,
    Content.SECURITY,
}


class TileSide(Enum):
    TOP = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 3


def create_tile(tile: MapTile) -> bytearray:
    gfx = bytearray([(COLOR_BG << 4) | COLOR_BG for _ in range(32)])

    # Handle tunnels separately
    if tile.content == Content.TUNNEL:
        draw_tunnel(gfx, tile.edges)
        if tile.transparent:
            make_transparent(gfx)
        return gfx

    # Corners
    if tile.corners.top_left:
        set_pixel(gfx, COLOR_WHITE_OUTLINE, 0, 0)
    if tile.corners.top_right:
        set_pixel(gfx, COLOR_WHITE_OUTLINE, 7, 0)
    if tile.corners.bottom_left:
        set_pixel(gfx, COLOR_WHITE_OUTLINE, 0, 7)
    if tile.corners.bottom_right:
        set_pixel(gfx, COLOR_WHITE_OUTLINE, 7, 7)

    # Edges
    for edge, side in zip(tile.edges, TileSide):
        if isinstance(edge, Edge):
            if edge == Edge.WALL:
                draw_wall(gfx, side)
            elif edge == Edge.DOOR:
                draw_connection(gfx, side)
            # TODO: Support Edge.SHORTCUT
        elif isinstance(edge, ColoredDoor):
            if edge == ColoredDoor.BLUE:
                draw_hatch_mf(gfx, COLOR_BLUE_EDGE, side)
            elif edge == ColoredDoor.GREEN:
                draw_hatch_mf(gfx, COLOR_GREEN_EDGE, side)
            elif edge == ColoredDoor.YELLOW:
                draw_hatch_mf(gfx, COLOR_YELLOW_EDGE, side)
            elif edge == ColoredDoor.RED:
                draw_hatch_mf(gfx, COLOR_RED_EDGE, side)
            # TODO: ZM hatch types

    # Content
    if tile.content in HAS_RED_OUTLINE:
        draw_red_outline(gfx, tile.edges)

    # The following don't have doors near them so they aren't needed:
    # Gunship, Animals, Boiler Pad
    match tile.content:
        case Content.NAVIGATION:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_NAVIGATION)
        case Content.SAVE:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_SAVE)
        case Content.RECHARGE:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_RECHARGE)
        case Content.HIDDEN_RECHARGE:
            draw_pixel_art(gfx, COLOR_YELLOW_HIDDEN, PIXELS_RECHARGE)
        case Content.DATA:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_DATA)
        case Content.ITEM:
            draw_pixel_art(gfx, COLOR_WHITE_ITEM, PIXELS_ITEM)
        case Content.OBTAINED_ITEM:
            draw_obtained_tank(gfx)
        case Content.BOSS_RIGHT_DOWNLOADED:
            draw_boss_room(gfx, COLOR_CONNECTION_BG, 2, 1)
        case Content.BOSS_BOTTOM_LEFT_BOTH:
            draw_boss_room(gfx, COLOR_WHITE_OUTLINE, 0, 2)
        case Content.BOSS_TOP_LEFT_BOTH:
            draw_boss_room(gfx, COLOR_WHITE_OUTLINE, 0, 0)
        case Content.BOSS_LEFT_BOTH:
            draw_boss_room(gfx, COLOR_WHITE_OUTLINE, 0, 1)
        case Content.BOSS_TOP_RIGHT_BOTH:
            draw_boss_room(gfx, COLOR_WHITE_OUTLINE, 2, 0)
        case Content.BOSS_TOP_RIGHT_EXPLORED:
            draw_boss_room(gfx, COLOR_WHITE_ITEM, 2, 0)
        case Content.GUNSHIP_EDGE:
            draw_gunship_edge(gfx)
        case Content.SECURITY:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_SECURITY)
        case Content.AUXILLARY_POWER:
            draw_pixel_art(gfx, COLOR_YELLOW_LETTER, PIXELS_AUXILIARY)
        case _:
            if tile.content != Content.EMPTY and tile.content != Content.EMPTY_RED_WALLS:
                raise ValueError(f"No implementation to create tile content {tile.content}")

    if tile.transparent:
        make_transparent(gfx)
    return gfx


def make_transparent(gfx: bytearray) -> None:
    for y in range(8):
        for x in range(8):
            color = get_pixel(gfx, x, y)
            if color == COLOR_BLANK_OUTLINE or color == COLOR_BLANK_BG:
                set_pixel(gfx, 0, x, y)


def get_pixel(gfx: bytearray, x: int, y: int) -> int:
    index = (y * 8 + x) // 2
    if x % 2 == 0:
        return gfx[index] & 0xF
    else:
        return gfx[index] >> 4


def set_pixel(gfx: bytearray, color: int, x: int, y: int) -> None:
    index = (y * 8 + x) // 2
    if x % 2 == 0:
        gfx[index] = (gfx[index] & 0xF0) | color
    else:
        gfx[index] = (gfx[index] & 0xF) | (color << 4)


def draw_pixel_art(gfx: bytearray, color: int, art: list[str]) -> None:
    for y, row in enumerate(art):
        for x, character in enumerate(row.replace(" ", "")):
            if character != ".":
                actual_color = COLOR_BG if character == "-" else color
                set_pixel(gfx, actual_color, x, y)


def draw_colored_pixel_art(gfx: bytearray, art: list[str]) -> None:
    for y, row in enumerate(art):
        for x, character in enumerate(row.replace(" ", "")):
            if character != ".":
                color = COLOR_BG if character == "-" else int(character, 16)
                set_pixel(gfx, color, x, y)


def draw_wall(gfx: bytearray, side: TileSide) -> None:
    additional_coordinate = 0 if side == TileSide.TOP or side == TileSide.LEFT else 7
    if side == TileSide.TOP or side == TileSide.BOTTOM:
        for x in range(8):
            set_pixel(gfx, COLOR_WHITE_OUTLINE, x, additional_coordinate)
    elif side == TileSide.LEFT or side == TileSide.RIGHT:
        for y in range(8):
            set_pixel(gfx, COLOR_WHITE_OUTLINE, additional_coordinate, y)


def draw_connection(gfx: bytearray, side: TileSide) -> None:
    draw_wall(gfx, side)

    if side == TileSide.TOP:
        set_pixel(gfx, COLOR_CONNECTION_BG, 3, 0)
        set_pixel(gfx, COLOR_CONNECTION_BG, 4, 0)
    elif side == TileSide.BOTTOM:
        set_pixel(gfx, COLOR_CONNECTION_BG, 3, 7)
        set_pixel(gfx, COLOR_CONNECTION_BG, 4, 7)
    elif side == TileSide.LEFT:
        set_pixel(gfx, COLOR_CONNECTION_BG, 0, 3)
        set_pixel(gfx, COLOR_CONNECTION_BG, 0, 4)
    elif side == TileSide.RIGHT:
        set_pixel(gfx, COLOR_CONNECTION_BG, 7, 3)
        set_pixel(gfx, COLOR_CONNECTION_BG, 7, 4)


def draw_hatch_mf(gfx: bytearray, color: int, side: TileSide) -> None:
    draw_wall(gfx, side)

    inner = color + COLOR_COUNT
    if side == TileSide.LEFT:
        set_pixel(gfx, color, 0, 3)
        set_pixel(gfx, color, 0, 4)
        set_pixel(gfx, inner, 1, 2)
        set_pixel(gfx, inner, 1, 3)
        set_pixel(gfx, inner, 1, 4)
        set_pixel(gfx, inner, 1, 5)
    elif side == TileSide.RIGHT:
        set_pixel(gfx, color, 7, 3)
        set_pixel(gfx, color, 7, 4)
        set_pixel(gfx, inner, 6, 2)
        set_pixel(gfx, inner, 6, 3)
        set_pixel(gfx, inner, 6, 4)
        set_pixel(gfx, inner, 6, 5)


def draw_hatch_zm(gfx: bytearray, color: int, side: TileSide) -> None:
    draw_wall(gfx, side)

    inner = color + COLOR_COUNT
    if side == TileSide.LEFT:
        set_pixel(gfx, color, 0, 3)
        set_pixel(gfx, color, 0, 4)
        set_pixel(gfx, COLOR_WHITE_ITEM, 1, 2)
        set_pixel(gfx, inner, 1, 3)
        set_pixel(gfx, inner, 1, 4)
        set_pixel(gfx, COLOR_WHITE_ITEM, 1, 5)
    elif side == TileSide.RIGHT:
        set_pixel(gfx, color, 7, 3)
        set_pixel(gfx, color, 7, 4)
        set_pixel(gfx, COLOR_WHITE_ITEM, 6, 2)
        set_pixel(gfx, inner, 6, 3)
        set_pixel(gfx, inner, 6, 4)
        set_pixel(gfx, COLOR_WHITE_ITEM, 6, 5)


def draw_obtained_tank(gfx: bytearray) -> None:
    set_pixel(gfx, COLOR_WHITE_ITEM, 3, 3)
    set_pixel(gfx, COLOR_WHITE_ITEM, 3, 4)
    set_pixel(gfx, COLOR_WHITE_ITEM, 4, 3)
    set_pixel(gfx, COLOR_WHITE_ITEM, 4, 4)


def draw_red_outline(gfx: bytearray, edges: TileEdges) -> None:
    if (isinstance(edges.left, Edge) and edges.left == Edge.EMPTY) or (
        isinstance(edges.right, Edge) and edges.right == Edge.EMPTY
    ):
        raise ValueError(
            "The current implementation for red outline minimap tiles only supports "
            "left and right edges being walls or doors"
        )

    # Check for top and bottom walls
    if edges.top == Edge.WALL:
        for x in range(1, 7):
            set_pixel(gfx, COLOR_RED_EDGE, x, 0)
    if edges.bottom == Edge.WALL:
        for x in range(1, 7):
            set_pixel(gfx, COLOR_RED_EDGE, x, 7)

    # Draw parts of left and right edges that are always there
    for y in [0, 1, 6, 7]:
        set_pixel(gfx, COLOR_RED_EDGE, 0, y)
        set_pixel(gfx, COLOR_RED_EDGE, 7, y)

    # Check for left wall
    if isinstance(edges.left, Edge) and edges.left == Edge.WALL:
        for y in range(2, 6):
            set_pixel(gfx, COLOR_RED_EDGE, 0, y)
    else:
        # Remove any inner hatch pixels
        for y in range(2, 6):
            set_pixel(gfx, COLOR_BG, 1, y)

    # Check for right wall
    if isinstance(edges.right, Edge) and edges.right == Edge.WALL:
        for y in range(2, 6):
            set_pixel(gfx, COLOR_RED_EDGE, 7, y)
    else:
        # Remove any inner hatch pixels
        for y in range(2, 6):
            set_pixel(gfx, COLOR_BG, 6, y)


def draw_boss_room(gfx: bytearray, color: int, x_offset: int, y_offset: int) -> None:
    # Offsets are relative to the icon being in the top left corner
    for y, row in enumerate(PIXELS_BOSS):
        for x, character in enumerate(row.replace(" ", "")):
            if character == "#":
                set_pixel(gfx, color, x + x_offset, y + y_offset)


def draw_gunship_edge(gfx: bytearray) -> None:
    set_pixel(gfx, COLOR_YELLOW_LETTER, 7, 5)


def draw_tunnel(gfx: bytearray, edges: TileEdges) -> None:
    if (isinstance(edges.left, Edge) and edges.left == Edge.DOOR) or isinstance(
        edges.left, ColoredDoor
    ):
        # Door on left, arrow faces right
        draw_colored_pixel_art(gfx, COLORED_PIXELS_TUNNEL)
        edge = edges.left
        x = 0
    elif (isinstance(edges.right, Edge) and edges.right == Edge.DOOR) or isinstance(
        edges.right, ColoredDoor
    ):
        # Door on right, arrow faces left
        flipped = [row[::-1] for row in COLORED_PIXELS_TUNNEL]
        draw_colored_pixel_art(gfx, flipped)
        edge = edges.right
        x = 7
    else:
        raise ValueError("Tunnel does not have any doors")

    color = -1
    if isinstance(edge, ColoredDoor):
        if edge == ColoredDoor.BLUE:
            color = COLOR_BLUE_EDGE
        elif edge == ColoredDoor.GREEN:
            color = COLOR_GREEN_EDGE
        elif edge == ColoredDoor.YELLOW:
            color = COLOR_YELLOW_EDGE
        elif edge == ColoredDoor.RED:
            color = COLOR_RED_EDGE

    if color != -1:
        set_pixel(gfx, color, x, 3)
        set_pixel(gfx, color, x, 4)
