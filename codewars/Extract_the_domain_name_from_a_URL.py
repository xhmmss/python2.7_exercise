# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# domain_name("https://www.cnet.com") == "cnet"

def domain_name_clever(url):

	return url.split('//')[-1].split('www.')[-1].split('.')[0]
	
print domain_name_clever("http://www.github.com/carbonfive/raygun")