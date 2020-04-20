import os

startComment = "START AUTO-INSERT HEAD"
endComment = "END AUTO-INSERT HEAD"
tempfile = 'nav.temp'

pagelist=["../opensource.html","../index.html","../competitiveprogramming.html","../blogs.html","../courses.html","../developerclubs.html","../elements.html","../internships.html","../research.html","../scholarships.html","../contribute.html"]
def updatePage():
  with open(pageToChange,'r') as file:
    orgLines = file.readlines()

  with open(pageToChange,'w') as file:
    write = True
    for x in orgLines:
      if endComment in x:
        write = True
        file.write('\n')
      if write:
        file.write(x)
      if startComment in x:
        with open(tempfile,'r') as temp:
          add = temp.read()
        file.write(add)
        write = False

with open(tempfile, 'w') as f:
    f.write('''
					<footer id="footer">
						<div class="inner">
							<section>
								<h2>Get in touch</h2>
								<ul class="icons">
									<li><a href="https://www.facebook.com/sonali.singhal.735944" class="icon brands style2 fa-facebook-f"><span class="label">Facebook</span></a></li>
									<li><a href="https://www.linkedin.com/in/sonalisinghal/" class="icon brands style2 fa-linkedin-in"><span class="label">LinkdIn/span></a></li>
									<li><a href="https://github.com/Sonalisinghal" class="icon brands style2 fa-github"><span class="label">GitHub</span></a></li>
									<li><a href="mailto:sonali.singal1999@gmail.com" class="icon solid style2 fa-envelope"><span class="label">gmail</span></a></li>
								</ul>
							</section>
							<ul class="copyright">
								<li>Made by Sonali Singhal</li><li>Design: <a href="http://html5up.net">HTML5 UP - Phantom</a></li>
							</ul>
						</div>
					</footer>''')
for pageToChange in pagelist:
  updatePage()

#remove <tempfile> as we don't need it anymore
os.remove(tempfile)

                