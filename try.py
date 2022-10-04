import Pcolors
from Pcolors.builder import build


e = Pcolors.cinput(
    "Hello: ",
    Pcolors.style(fg_color=Pcolors.shortcuts.light.green),
    Pcolors.style(fg_color=Pcolors.shortcuts.light.blue),
)

print(e)

print(
    build(
        """
<c underline rgb_fg=(214,82,247)>
	hello
	<c underline=false crossed rgb_fg=(214,82,0) />
	not bold
</c> bob
			""".strip(),
        trim=False,
    )
)
