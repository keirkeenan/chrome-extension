# disable the following pylint warnings:
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=wrong-import-position

import unittest
from unittest.mock import patch
from web_scraper.main import get_html, parse_itemprice, scrape_ebay, scrape_walmart, scrape_amazon, scrape, scrape_all


class TestMethods(unittest.TestCase):
    # Test the get_html function

    def test_ebay(self):
        # Test with valid input
        html = get_html("ebay", "pencil", 1)
        self.assertTrue("<!DOCTYPE html>" in html)

    # def test_walmart(self):
    #     # Test with valid input
    #     html = get_html("walmart", "pencil", 1)
    #     self.assertTrue("<!DOCTYPE html>" in html)

    def test_amazon(self):
        # Test with valid input
        html = get_html("amazon", "pencil", 1)
        self.assertTrue("<!doctype html>" in html)

    def test_wrong_company_name(self):
        # Test with invalid input
        html = get_html("wrong", "pencil", 1)
        self.assertEqual(html, "Something went wrong. Please try again.")

    # ===================================#

    # Test the parse_itemprice function

    def test_parse_itemprice_valid(self):
        # Test with valid input
        result = parse_itemprice("$123.45")
        expected_output = 123.45
        self.assertEqual(result, expected_output)

    # ===================================#

    # Test the scrape functions

    def test_scrape_ebay_valid(self):
        # Test with valid input
        result = scrape_ebay("pencil")
        not_expected_output = "Failed to collect data from eBay. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)

    def test_scrape_walmart_mock(self):
        # Set up mock response for get_html
        mock_html = '<!DOCTYPE html><body><div class="mb0 ph1 pa0-xl bb b--near-white w-25"><div style="contain-intrinsic-size:198px 340px" class="h-100 pb1-xl pr4-xl pv3 ph1"><div data-item-id="1ZH03JCE3JSS" class="sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity"><a link-identifier="14977443" href="https://wrd.walmart.com/track?adUid=4c7a1615-1b6c-4743-a0ed-a18fcbd6bf6b&amp;pgId=pencil&amp;spQs=t8GXwbg0EFm3fn92HprVu77SJYyqzBpnp0an539TanzxdqlqncZUo3saIZZU1jMbu79F6El8NbCEG68wk4Nku1ETMd73EoAVCqjR-ce-MXNbODLGAi_LKmNvHR1khRCvjb3pDTDSIJNvqFpKkgGWMU2oy69l3DtcGtbDnLCnIZ_0H1eELCYiv5Mxz-lgO0O5i2PwnwAV0VyHD3AlOIF-F3ZhzAGPlO-8kIHU13-3ejo&amp;storeId=3520&amp;pt=search&amp;mloc=sp-search-middle&amp;bkt=2654&amp;pltfm=desktop&amp;rdf=1&amp;plmt=sp-search-middle~desktop~&amp;eventST=click&amp;pos=2&amp;bt=1&amp;tax=1229749_1431586_6267234_1778429&amp;et=head_torso&amp;st=torso&amp;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FBIC-Xtra-Strong-Thick-Lead-Mechanical-Pencil-Black-Thick-Point-0-9mm-24-Count%2F14977443%3Fathbdg%3DL1600%26adsRedirect%3Dtrue&amp;couponState=na&amp;athbdg=L1600" class="absolute w-100 h-100 z-1 hide-sibling-opacity" target=""><span class="w_iUH7">BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count<!-- --> </span></a><div class="" data-testid="list-view"><div class=""><div class="h2 relative mb2"><span class="w_VbBP w_mFV6 w_awtt w_3oNC w_3H8O absolute tag-leading-badge">Best seller</span></div><div class="relative"><div class="relative overflow-hidden" style="max-width:290px;height:0;padding-bottom:min(392px, 135.17241379310346%);align-self:center;width:min(290px, 100%)"><img loading="eager" width="" height="" class="absolute top-0 left-0" data-testid="productTileImage" alt="BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count" src="https://i5.walmartimages.com/asr/7691c1c3-3b23-418b-9591-2bd707d211b3.43afcf901046d245d286f2b94f582190.png?odnHeight=784&amp;odnWidth=580&amp;odnBg=FFFFFF"/></div><div class="z-2 absolute bottom--1"><div class="relative dib"><a class="w_hhLG w_8nsR w_jDfj pointer bn sans-serif b ph2 flex items-center justify-center w-auto shadow-1" href="https://wrd.walmart.com/track?adUid=4c7a1615-1b6c-4743-a0ed-a18fcbd6bf6b&amp;pgId=pencil&amp;spQs=t8GXwbg0EFm3fn92HprVu77SJYyqzBpnp0an539TanzxdqlqncZUo3saIZZU1jMbu79F6El8NbCEG68wk4Nku1ETMd73EoAVCqjR-ce-MXNbODLGAi_LKmNvHR1khRCvjb3pDTDSIJNvqFpKkgGWMU2oy69l3DtcGtbDnLCnIZ_0H1eELCYiv5Mxz-lgO0O5i2PwnwAV0VyHD3AlOIF-F3ZhzAGPlO-8kIHU13-3ejo&amp;storeId=3520&amp;pt=search&amp;mloc=sp-search-middle&amp;bkt=2654&amp;pltfm=desktop&amp;rdf=1&amp;plmt=sp-search-middle~desktop~&amp;eventST=click&amp;pos=2&amp;bt=1&amp;tax=1229749_1431586_6267234_1778429&amp;et=head_torso&amp;st=torso&amp;rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FBIC-Xtra-Strong-Thick-Lead-Mechanical-Pencil-Black-Thick-Point-0-9mm-24-Count%2F14977443%3Fathbdg%3DL1600%26adsRedirect%3Dtrue&amp;couponState=na&amp;athbdg=L1600" aria-label="Options - BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count"><span class="mh2">Options</span></a></div></div></div><div class="mt5 mb0" style="height:24px" data-testid="variant-1ZH03JCE3JSS"><div class="flex items-center lh-title h2-l normal"><span class="gray f7">Sponsored</span></div></div></div><div class=""><div data-automation-id="product-price" class="flex flex-wrap justify-start items-center lh-title mb1"><div class="mr1 mr2-xl b black green lh-copy f5 f4-l" aria-hidden="true">Now $6.22</div><span class="w_iUH7">current price Now $6.22</span><div class="gray mr1 strike f7 f6-l" aria-hidden="true">$11.26</div><span class="w_iUH7">Was $11.26</span><div class="f7 f6-l gray mr1">$6.22/ea</div></div><span class="w_V_DM" style="-webkit-line-clamp:3;padding-bottom:0em;margin-bottom:-0em"><span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">BIC Xtra-Strong Thick Lead Mechanical Pencil, Black, Thick Point (0.9mm), 24-Count</span></span><div class="flex items-center mt2"><span class="black inline-flex mr1"><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarFill" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i><i class="ld ld-StarHalf" style="font-size:12px;vertical-align:-0.175em;width:12px;height:12px;box-sizing:content-box" aria-hidden="true"></i></span><span class="sans-serif gray f7" aria-hidden="true">147</span><span class="w_iUH7">4.7 out of 5 Stars. 147 reviews</span></div><div></div><div class="flex items-center mv2"><div class="f7 mr1 blue b lh-copy">Save with</div><img loading="lazy" class="flex" src="//i5.walmartimages.com/dfw/63fd9f59-ac39/29c6759d-7f14-49fa-bd3a-b870eb4fb8fb/v1/wplus-icon-blue.svg" alt="Walmart Plus" height="20" width="20"/></div><div class="mt2 mb2"><span class="w_VbBP w_mFV6 w_I_19 w_3oNC w_AAn7 mr1 mt1 ph1">Pickup</span><span class="w_VbBP w_mFV6 w_I_19 w_3oNC w_AAn7 mr1 mt1 ph1">2-day shipping</span></div></div></div></div></div></div></body></html>'
        with patch("web_scraper.main.get_html", return_value=mock_html):
            # Test with valid input
            result = scrape_walmart("pencil")
            not_expected_output = "Failed to collect data from Walmart. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
            self.assertNotEqual(result, not_expected_output)

    def test_scrape_amazon_valid(self):
        # Set up mock response for get_html
        mock_html = '<!doctype html><body><div data-asin="B09LP7YLF9" data-index="8" data-uuid="2b3e8c40-4d06-4cf7-9809-301b4946a023" data-component-type="s-search-result" class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-8" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_38" data-csa-c-pos="38" data-csa-c-item-id="amzn1.asin.1.B09LP7YLF9" data-csa-op-log-render="" data-csa-c-type="item"><div class="s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis s-latency-cf-section s-card-border"><div class="a-section"><div class="sg-row"><div class="sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 sg-col-4-of-24 s-list-col-left"><div class="sg-col-inner"><div class="a-section a-spacing-none aok-relative puis-status-badge-container s-list-status-badge-container"></div><div class="s-product-image-container aok-relative s-text-center s-image-overlay-grey s-padding-left-small s-padding-right-small s-flex-expand-height"><div class="aok-relative"><span data-component-type="s-product-image" class="rush-component"><a class="a-link-normal s-no-outline" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=sr_1_38?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38"><div class="a-section aok-relative s-image-fixed-height"><img class="s-image" src="https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY218_.jpg" srcset="https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY218_.jpg 1x, https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY327_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY436_QL65_.jpg 2x, https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY545_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/61bF9WNs7dL._AC_UY654_QL65_.jpg 3x" alt="Apple iPhone 13 Pro, 128GB, Gold - Unlocked (Renewed)" data-image-index="38" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"/></div></a></span></div></div></div></div><div class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right"><div class="sg-col-inner"><div class="a-section a-spacing-small a-spacing-top-small"><div class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style"><h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=sr_1_38?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38"><span class="a-size-medium a-color-base a-text-normal">Apple iPhone 13 Pro, 128GB, Gold - Unlocked (Renewed)</span> </a> </h2></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-small"><span aria-label="4.3 out of 5 stars"><span class="a-declarative" data-action="a-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-a-popover" data-a-popover="{&quot;closeButton&quot;:false,&quot;closeButtonLabel&quot;:&quot;&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;popoverLabel&quot;:&quot;&quot;,&quot;url&quot;:&quot;/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&amp;asin=B09LP7YLF9&amp;ref=acr_search__popover&amp;contextId=search&quot;}"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative"><i class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"><span class="a-icon-alt">4.3 out of 5 stars</span></i><i class="a-icon a-icon-popover"></i></a></span> </span><span aria-label="809"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=sr_1_38?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38#customerReviews"><span class="a-size-base s-underline-text">809</span> </a> </span></div></div><div class="sg-row"><div class="sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 sg-col-4-of-24"><div class="sg-col-inner"><div class="a-section a-spacing-none a-spacing-top-micro s-price-instructions-style"><div class="a-row a-size-base a-color-base"><a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=sr_1_38?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38"><span class="a-price" data-a-size="xl" data-a-color="base"><span class="a-offscreen">$768.00</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">768<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span> </a> <span class="a-letter-space"></span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-row a-size-base a-color-secondary s-align-children-center"><span aria-label="FREE delivery May 3 - 4 "><span class="a-color-base">FREE delivery </span><span class="a-color-base a-text-bold">May 3 - 4 </span></span></div><div class="a-row a-size-base a-color-secondary"><span aria-label="Only 8 left in stock - order soon."><span class="a-size-base a-color-price">Only 8 left in stock - order soon.</span></span></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div data-csa-c-type="element" data-csa-c-content-id="variation-options-link" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" class="s-variations-options-justify-content"><span class="a-size-small s-variation-options-text s-variations-options-justify-content"><div class="s-variation-options-options-text aok-inline-block">Options:</div><a class="a-size-small a-align-top a-link-normal s-variation-options-link aok-inline-block a-nowrap" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=vo_sr_l_dp?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="link"><span class="a-truncate" data-a-word-break="normal" data-a-max-rows="1" data-a-overflow-marker="&amp;hellip;" style="line-height: 1.3em !important; max-height: 1.3em;"><span class="a-truncate-full">4 sizes</span><span class="a-truncate-cut a-hidden" aria-hidden="true"></span></span></a></span></div></div><div class="a-section a-spacing-none a-spacing-top-micro"><div class="a-section a-spacing-none s-align-children-center"><div><div class="s-align-children-center"><span class="a-declarative" data-action="s-pc-popover" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-pc-popover" data-s-pc-popover="{&quot;closeButton&quot;:true,&quot;closeButtonLabel&quot;:&quot;Close popup&quot;,&quot;activate&quot;:&quot;onclick&quot;,&quot;name&quot;:&quot;pc-popover-B09LP7YLF9&quot;,&quot;width&quot;:339,&quot;popoverLabel&quot;:&quot;Provenance certifications for this product&quot;,&quot;position&quot;:&quot;triggerBottom&quot;,&quot;interactLoggingMetricsList&quot;:[&quot;provenanceCertifications_desktop_cpf_badge&quot;]}"><a href="javascript:void(0)" role="button" class="a-popover-trigger a-declarative s-no-underline s-pc-badge s-align-children-center"><span class="faceout-image-view"></span><img alt="" src="https://m.media-amazon.com/images/I/216-OX9rBaL._SS200_.png" class="s-image" height="18px" width="18px"/>  <span class="a-size-base a-color-base">Climate Pledge Friendly</span><i class="a-icon a-icon-popover"></i></a></span></div></div></div><div class="a-popover-preload" id="a-popover-pc-popover-B09LP7YLF9"><div class="puis"><div class="s-align-children-center"><div class="s-align-children-center"><span class="faceout-image-view"></span><div alt="" style="height:50px;width:50px;" class="a-image-wrapper a-lazy-loaded a-manually-loaded s-image" data-a-image-source="https://m.media-amazon.com/images/I/216-OX9rBaL._SS200_.png"><noscript><img alt="" src="https://m.media-amazon.com/images/I/216-OX9rBaL._SS200_.png" height="50px" width="50px"/></noscript></div>  <span class="a-size-base a-color-base a-text-bold">Climate Pledge Friendly</span></div></div><div class="a-spacing-small"><span class="a-size-base a-color-secondary">Products with trusted sustainability certification(s).</span> <a class="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style" href="/climatepledgefriendly">Learn more</a> </div><div class="a-spacing-small"><span class="a-size-base a-color-tertiary a-text-bold">Product Certification (1)</span></div><div class="a-spacing-small s-align-children-center s-pc-certification"><div class="s-pc-certification-logo aok-inline-block"><span class="faceout-image-view"></span><div alt="" style="height:50px;width:50px;" class="a-image-wrapper a-lazy-loaded a-manually-loaded s-image" data-a-image-source="https://m.media-amazon.com/images/I/51-8sbqIQBL._SS200_.jpg"><noscript><img alt="" src="https://m.media-amazon.com/images/I/51-8sbqIQBL._SS200_.jpg" height="50px" width="50px"/></noscript></div> </div><div class="a-section s-margin-bottom-none aok-inline-block"><span class="a-color-base a-text-bold">Pre-owned Certified</span> <span class="a-color-base"> products are inspected, cleaned and (if applicable) repaired to excellent functional standards. Buying Pre-owned extends a product&#x27;s life, reducing e-waste and raw material extraction.</span></div></div></div></div></div><div class="a-section a-spacing-none a-spacing-top-mini"><div class="a-row a-size-base a-color-secondary"><span class="a-size-base a-color-secondary">More Buying Choices</span><br/><span class="a-color-base">$714.99</span><span class="a-letter-space"></span><span class="a-declarative" data-action="s-show-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-s-show-all-offers-display" data-s-show-all-offers-display="{&quot;assetMismatch&quot;:&quot;Abandon&quot;,&quot;fallbackUrl&quot;:&quot;/gp/offer-listing/B09LP7YLF9/ref=sr_1_38_olp?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38&quot;,&quot;url&quot;:&quot;/gp/aod/ajax/ref=sr_1_38_aod?asin=B09LP7YLF9&amp;pc=sp&amp;keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38&amp;rrid=59JZH6JT3JTM2EBAREAE&quot;}"><a class="a-link-normal s-link-style s-underline-text s-underline-link-text" href="/gp/offer-listing/B09LP7YLF9/ref=sr_1_38_olp?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38">(16 used &amp; new offers)</a></span> <div id="all-offers-display" class="a-section aok-hidden"><div id="all-offers-display-spinner" class="a-spinner-wrapper aok-hidden"><span class="a-spinner a-spinner-medium"></span></div></div><span class="a-declarative" data-action="close-all-offers-display" data-csa-c-type="widget" data-csa-c-func-deps="aui-da-close-all-offers-display"><div id="aod-background" class="a-section aok-hidden aod-darken-background"></div></span></div></div><div class="a-section a-spacing-none a-spacing-top-mini s-color-swatch-container-list-view"><div class="a-section s-color-swatch-container s-quick-view-text-align-start"><div class="a-section s-color-swatch-outer-circle s-color-swatch-pad s-color-swatch-outer-circle-selected"><div data-csa-c-swatch-url="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=cs_sr_dp_1?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" data-csa-c-type="link" data-csa-c-content-id="color-swatch-link" data-csa-c-swatch-position="1" data-csa-c-swatch-is-selected="true" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" data-csa-c-interaction-events="click"><a aria-label="Gold" class="a-link-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LP7YLF9/ref=cs_sr_dp_1?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="button"><span class="s-color-swatch-inner-circle-fill" style="background-color: #EDD9C3"><span class="s-color-swatch-inner-circle-border"></span></span></a></div></div><div class="a-section s-color-swatch-outer-circle s-color-swatch-pad"><div data-csa-c-swatch-url="/Apple-iPhone-13-Pro-128GB/dp/B09LPJRKKB/ref=cs_sr_dp_2?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" data-csa-c-type="link" data-csa-c-content-id="color-swatch-link" data-csa-c-swatch-position="2" data-csa-c-swatch-is-selected="false" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" data-csa-c-interaction-events="click"><a aria-label="Graphite" class="a-link-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LPJRKKB/ref=cs_sr_dp_2?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="button"><span class="s-color-swatch-inner-circle-fill" style="background-color: #4A4946"><span class="s-color-swatch-inner-circle-border"></span></span></a></div></div><div class="a-section s-color-swatch-outer-circle s-color-swatch-pad"><div data-csa-c-swatch-url="/Apple-iPhone-13-Pro-128GB/dp/B09LPCW6LH/ref=cs_sr_dp_3?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" data-csa-c-type="link" data-csa-c-content-id="color-swatch-link" data-csa-c-swatch-position="3" data-csa-c-swatch-is-selected="false" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" data-csa-c-interaction-events="click"><a aria-label="Sierra Blue" class="a-link-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LPCW6LH/ref=cs_sr_dp_3?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="button"><span class="s-color-swatch-inner-circle-fill" style="background-color: #8CA9BF"><span class="s-color-swatch-inner-circle-border"></span></span></a></div></div><div class="a-section s-color-swatch-outer-circle s-color-swatch-pad"><div data-csa-c-swatch-url="/Apple-iPhone-13-Pro-128GB/dp/B09LPNMW8J/ref=cs_sr_dp_4?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" data-csa-c-type="link" data-csa-c-content-id="color-swatch-link" data-csa-c-swatch-position="4" data-csa-c-swatch-is-selected="false" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" data-csa-c-interaction-events="click"><a aria-label="Silver" class="a-link-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09LPNMW8J/ref=cs_sr_dp_4?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="button"><span class="s-color-swatch-inner-circle-fill" style="background-color: #E4E6E0"><span class="s-color-swatch-inner-circle-border"></span></span></a></div></div><div class="a-section s-color-swatch-outer-circle s-color-swatch-pad"><div data-csa-c-swatch-url="/Apple-iPhone-13-Pro-128GB/dp/B09YL28WK9/ref=cs_sr_dp_5?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" data-csa-c-type="link" data-csa-c-content-id="color-swatch-link" data-csa-c-swatch-position="5" data-csa-c-swatch-is-selected="false" data-csa-c-device-type="DESKTOP" data-csa-c-device-env="WEB" data-csa-c-device-os="UNRECOGNIZED" data-csa-c-interaction-events="click"><a aria-label="Alpine Green" class="a-link-normal" href="/Apple-iPhone-13-Pro-128GB/dp/B09YL28WK9/ref=cs_sr_dp_5?keywords=iphone+12&amp;qid=1682624823&amp;sr=8-38" role="button"><span class="s-color-swatch-inner-circle-fill" style="background-color: #414D41"><span class="s-color-swatch-inner-circle-border"></span></span></a></div></div></div></div></div></div><div class="sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-8-of-20 sg-col-8-of-24"><div class="sg-col-inner"></div></div></div></div></div></div></div></div></div></div></div></div></body></html>'
        with patch("web_scraper.main.get_html", return_value=mock_html):
            # Test with valid input
            result = scrape_amazon("iphone 12")
            not_expected_output = "Failed to collect data from Amazon. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
            self.assertNotEqual(result, not_expected_output)

    # ===================================#

    # Test the main function

    def test_main_valid(self):
        # Test with valid input
        result = scrape("pencil", "ebay")
        not_expected_output = "Failed to collect data from eBay."
        self.assertNotEqual(result, not_expected_output)

    def test_main_invalid(self):
        # Test with invalid input
        result = scrape("pencil", "Random Company")
        expected_output = "Scraper not available for `Random Company`. Try: eBay, Walmart, or Amazon."
        self.assertEqual(result, expected_output)

    # ===================================#

    # Test the scrape_all function

    def test_scrape_all_success(self):
        # Test with valid input
        result = scrape_all("pencil")
        not_expected_output = "Failed to collect any data. Please try again or post an issue on GitHub: https://github.com/keirkeenan/web-scraper-python-library/issues/new"
        self.assertNotEqual(result, not_expected_output)


if __name__ == "__main__":
    unittest.main()
