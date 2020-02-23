from pattern.web import URL, DOM
import re

class YouTubeHandler(object):

    def __init__(self, Key = '' ):
        self.Title = Key
        self.prefix_of_search_url = "https://www.youtube.com/results?search_query="
        self.target_yt_search_url_str = ''
        self.filter_url_portion = '&filters=playlist'
        self.page_url_portion = '' 
        self.video_link_title_dict = {} 
        self.video_link_title_keylist = []
        self.link = str()

    def reformat_search_for_spaces(self):
        self.Title = self.Title.rstrip().replace(' ', '+')

    def form_search_url(self):
        self.reformat_search_for_spaces()
        self.target_yt_search_url_str = self.prefix_of_search_url + self.Title + self.filter_url_portion 

    def get_dom_object(self, url_target):
        try:
            url = URL(url_target)
            dom_object = DOM(url.download(cached=True))
        except:
            print ('Problem retrieving data for this url: ', self.target_url_str)
            self.url_query_timeout = 1
        return dom_object       

    def tag_element_results(self, dom_obj, tag_expr):
        return dom_obj(tag_expr)

    def get_individual_video_link(self):
        self.filter_url_portion = '' 
        target_search_results_obj = []
        self.page_url_portion = '&page=1'
        self.form_search_url()
        search_result_dom = self.get_dom_object(self.target_yt_search_url_str)
        target_search_results_obj.extend(self.tag_element_results(search_result_dom, 'div[class="yt-lockup-content"] h3[class="yt-lockup-title"] a'))
        each_video_link_title_dict = {}

        for n in target_search_results_obj:
            video_link = n.attributes['href']
            video_link = re.sub('watch\?v=',r'watch?v=',video_link)
            
            video_title = n.attributes['title']
            each_video_link_title_dict[video_title] = 'https://www.youtube.com' + video_link
            self.link = 'https://www.youtube.com' + video_link
            break

