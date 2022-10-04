from unittest import TestCase

from Pcolors.builder import build


class Test(TestCase):
	def test_build(self):
		self.assertEqual(
			build("""
			<!--html-->
			<c underline rgb_fg=(214,82,247)>
				hello
				<c underline=false crossed rgb_fg=(214,82,0) />
				not bold
			</c>
			"""),
			"[0m[39;49;4;38;2;214;82;247mhello[0m[39;49;9;38;2;214;82;0mnot bold[0m"
		)
		self.assertEqual(
			build("""
				<c underline rgb_fg=(214,82,247)>
					hello
					<c underline=false crossed rgb_fg=(214,82,0) />
					not bold
				</c>""", trim=False
			),"""
				[0m[39;49;4;38;2;214;82;247m
					hello
					[0m[39;49;9;38;2;214;82;0m
					not bold
				[0m"""
		)
		self.assertEqual(
			build("""
					<!--html-->
					<c underline rgb_fg=(214,82,247)>
						hello
						<c underline=false crossed rgb_fg=(214,82,0) />
						not bold
					</c>
					"""),
			"[0m[39;49;4;38;2;214;82;247mhello[0m[39;49;9;38;2;214;82;0mnot bold[0m"
		)