# import colorama

# colorama.init()

def preview():
	print("""
Test of the colors:

	foreground:
		light:
			\033[90m black\033[0m \033[94m  blue \033[0m  
			\033[91m red\033[0m \033[95m    magenta\033[0m  
			\033[92m green\033[0m \033[96m  cyan\033[0m 
			\033[93m yellow\033[0m \033[97m white\033[0m 
		dark:
			\033[30m lblack\033[0m\033[34m   lblue \033[0m  
			\033[31m lred\033[0m \033[35m    lmagenta\033[0m  
			\033[32m lgreen\033[0m \033[36m  lcyan\033[0m 
			\033[33m lyellow\033[0m \033[37m lwhite\033[0m 
	background:
		light:
			\033[100m black  \033[0m \033[104mblue     \033[0m  
			\033[101m red    \033[0m \033[105mmagenta  \033[0m  
			\033[102m green  \033[0m \033[106mcyan     \033[0m 
			\033[103m yellow \033[0m \033[107mwhite    \033[0m 
		dark:
			\033[40m lblack \033[0m \033[44mlblue    \033[0m  
			\033[41m lred   \033[0m \033[45mlmagenta \033[0m  
			\033[42m lgreen \033[0m \033[46mlcyan    \033[0m 
			\033[43m lyellow\033[0m \033[47mlwhite   \033[0m 
	fore:
			\033[0m normal      \033[0m \033[1mbold           \033[0m
			\033[2m faint       \033[0m \033[4munderline      \033[0m 
			\033[5m slow_blink  \033[0m \033[9mcrossed        \033[0m  
			\033[6m rapid_blink \033[0m \033[21munderline_bold \033[0m  
			\033[7m reverse     \033[0m \033[51mframed         \033[0m 
			\033[8m hidden      \033[0m \033[52mrounded        \033[0m 
			\033[3m italic      \033[0m
			
	combo:
		\033[42;31;1;51m background lgreen, foreground red, bold,  framed \033[0m
		\033[42;31;51m background lgreen, foreground red,        framed \033[0m
		\033[42;30;51m background lgreen, foreground black,      framed \033[0m
		\033[42;30;51;2m background lgreen, foreground black,      framed, faint \033[0m
		\033[42;36;7m background lgreen, foreground cyan,      reverse \033[0m
		\033[51;1;3;4;9m framed, bold, italic, underline, crossed \033[0m
		
		
	\033[5;90;1;21ma\033[91mm\033[92ma\033[93mz\033[94mi\033[95mn\033[96mg \033[90m& \033[91ma \033[92mlo\033[93mt \033[94mmo\033[95mre\033[96m t\033[97mo \033[90mdi\033[91msc\033[92mov\033[93mer\033[0m
	
	\033[31;1m!\033[0m\033[90;2;3m the result can be diferent depending on the terminal you use and the theme\033[0m \033[31;1m¡\033[0m

""")
