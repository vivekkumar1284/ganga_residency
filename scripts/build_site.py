#!/usr/bin/env python3
"""Transform copied Ganga County pages into Ganga Residency starter site."""

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

BRAND_LINK = '<a href="index.html" class="brand-logo"><span class="brand-logo-text">Ganga Residency</span></a>'
FOOTER_BRAND = '<a href="index.html"><span class="brand-logo-text">Ganga Residency</span></a>'

PRICING_BLOCK_INDEX = """                        <div class="row justify-content-center">
                            <div class="col-lg-4 col-md-6 col-sm-12">
                                <div class="renvia-pricing-item style-one mb-40" data-aos="fade-up" data-aos-duration="1000">
                                    <div class="pricing-header mb-35">
                                        <span class="plan">100 Sq.Yd.</span>
                                        <div class="price">₹ <span>16,500</span><small>/Sq.Yd.</small></div>
                                        <p>Effective Pre-Launch Price</p>
                                    </div>
                                    <div class="pricing-button mb-40">
                                        <a href="contact.html" class="theme-btn style-one" style="color: #fff;">Request A Call<i class="fa-solid fa-arrow-right"></i></a>
                                    </div>
                                    <div class="pricing-body">
                                        <ul class="check-list style-one">
                                            <li class="check"><i class="iconoir-badge-check"></i>100 Sq.Yd. Plot</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>Launch: ₹17,500/Sq.Yd.</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>Pre-Launch Discount: ₹1,000/Sq.Yd.</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>25 &amp; 30 ft Internal Roads</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 col-sm-12">
                                <div class="renvia-pricing-item style-one mb-40 popular-plan" data-aos="fade-up" data-aos-duration="1200">
                                    <div class="pricing-header mb-35">
                                        <span class="plan">150 Sq.Yd.</span>
                                        <div class="price">₹ <span>16,500</span><small>/Sq.Yd.</small></div>
                                        <p>Effective Pre-Launch Price</p>
                                    </div>
                                    <div class="pricing-button mb-40">
                                        <a href="contact.html" class="theme-btn style-one">Request A Call<i class="fa-solid fa-arrow-right"></i></a>
                                    </div>
                                    <div class="pricing-body">
                                        <ul class="check-list style-one">
                                            <li class="check"><i class="iconoir-badge-check"></i>150 Sq.Yd. Plot</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>Launch: ₹17,500/Sq.Yd.</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>Pre-Launch Discount: ₹1,000/Sq.Yd.</li>
                                            <li class="check"><i class="iconoir-badge-check"></i>1 Tree With Every Plot</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="pricing-note" data-aos="fade-up" data-aos-duration="1000">
                            <p><strong>15 Acre Plotted Township</strong> &mdash; Society internal roads 25 ft &amp; 30 ft wide.</p>
                            <p>Launch price ₹17,500/Sq.Yd. | Pre-launch discount ₹1,000/Sq.Yd. | <strong>Effective pre-launch price ₹16,500/Sq.Yd.</strong></p>
                        </div>"""

AMENITIES_SLIDER = """                                    <div class="choose-slider" data-aos="fade-up" data-aos-duration="1200">
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon1.png" alt="icon"></div><div class="content"><h5>Luxury Clubhouse</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon7.png" alt="icon"></div><div class="content"><h5>All Weather Swimming Pool</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon4.png" alt="icon"></div><div class="content"><h5>Indoor Badminton Court</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon3.png" alt="icon"></div><div class="content"><h5>Indoor Games Room</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon2.png" alt="icon"></div><div class="content"><h5>Gym</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon5.png" alt="icon"></div><div class="content"><h5>Library</h5></div></div>
                                        <div class="renvia-choose-box"><div class="icon"><img src="assets/images/home-three/icon/icon8.png" alt="icon"></div><div class="content"><h5>Restaurant</h5></div></div>
                                    </div>"""

PROJECT_SLIDER = """                        <div class="row justify-content-center project-image-grid g-4" data-aos="fade-up" data-aos-duration="1000">
                            <div class="col-md-6"><img src="assets/images/project/location1.jpeg" alt="Ganga Residency project location"></div>
                            <div class="col-md-6"><img src="assets/images/project/location2.jpeg" alt="Ganga Residency project location"></div>
                        </div>"""


def replace_logo(html: str) -> str:
    html = re.sub(
        r'<a href="index\.html" class="brand-logo"><img src="assets/images/home-one/logo/logo-main\.png" alt="Brand Logo"></a>',
        BRAND_LINK,
        html,
    )
    html = re.sub(
        r'<a href="index\.html"><img src="assets/images/home-one/logo/logo-white\.png"alt="Brand Logo"></a>',
        FOOTER_BRAND,
        html,
    )
    html = re.sub(
        r'<a href="index\.html"><img src="assets/images/home-one/logo/logo-white\.png" alt="Brand Logo"></a>',
        FOOTER_BRAND,
        html,
    )
    return html


def remove_nav_items(html: str) -> str:
    html = re.sub(
        r'\s*<li class="menu-item"><a href="assets/images/Ganga-Residency-Brochure\.pdf" target="_blank">Residential</a></li>\s*',
        "\n",
        html,
    )
    html = re.sub(
        r'\s*<li class="menu-item"><a href="assets/images/ATOM-City-Centre-by-Atomoney\.pdf" target="_blank">Commercial</a></li>\s*',
        "\n",
        html,
    )
    return html


def add_residency_css(html: str) -> str:
    if "residency.css" in html:
        return html
    return html.replace(
        '<link rel="stylesheet" href="assets/css/style.css">',
        '<link rel="stylesheet" href="assets/css/style.css">\n    <link rel="stylesheet" href="assets/css/residency.css">',
    )


def swap_project_images(html: str) -> str:
    html = re.sub(
        r'<div class="projects-slider-two"[\s\S]*?</div>\s*</div>\s*</section>',
        PROJECT_SLIDER + "\n                    </div>\n                </section>",
        html,
        count=1,
    )
    replacements = {
        "assets/images/home-one/hero/hero-bg1.jpg": "assets/images/project/location1.jpeg",
        "assets/images/home-one/hero/hero-bg2.jpg": "assets/images/project/location2.jpeg",
        "assets/images/home-one/hero/hero-bg3.jpg": "assets/images/project/location1.jpeg",
        "assets/images/innerpage/about/about-img1.jpg": "assets/images/project/location1.jpeg",
        "assets/images/innerpage/about/about-img2.jpg": "assets/images/project/location2.jpeg",
        "assets/images/innerpage/gallery/choose-img1.jpg": "assets/images/project/location2.jpeg",
        "assets/images/innerpage/gallery/work-img1.jpg": "assets/images/project/location1.jpeg",
        "assets/images/home-three/gallery/counter-img2.jpg": "assets/images/project/location2.jpeg",
        "assets/images/innerpage/bg/page-bg.jpg": "assets/images/project/location1.jpeg",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    return html


def replace_pricing_section(html: str) -> str:
    return re.sub(
        r'<div class="row justify-content-center">\s*<div class="col-lg-3 col-md-6 col-sm-12">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>\s*<!--======  End Pricing Section',
        PRICING_BLOCK_INDEX + "\n                    </div>\n                </section>\n                <!--======  End Pricing Section",
        html,
        count=1,
    )


def replace_amenities_slider(html: str) -> str:
    return re.sub(
        r'<div class="choose-slider"[\s\S]*?</div>\s*<div class="choose-arrows"',
        AMENITIES_SLIDER + '\n                                    <div class="choose-arrows"',
        html,
        count=1,
    )


def remove_sections(html: str) -> str:
    html = re.sub(
        r'<!--======  Start Blog Section  ======-->[\s\S]*?<!--======  End Blog Section  ======-->\s*',
        "",
        html,
    )
    html = re.sub(
        r'<!--======  Start Choose Section  ======-->[\s\S]*?<!--======  End Choose Section  ======-->\s*',
        "",
        html,
    )
    return html


def update_content(html: str) -> str:
    html = html.replace(
        "Government-approved residential and commercial plots at Ganga Residency, Garhmukteshwar. Plot sizes 100–150 Sq.Yd. Starting at ₹20,000 per Sq.Yd.",
        "Ganga Residency is a 15 acre plotted township in Garhmukteshwar with 100–150 Sq.Yd. plots. Effective pre-launch price ₹16,500 per Sq.Yd.",
    )
    html = html.replace(
        "Key Features of Ganga Residency Residential Plots:",
        "Key Features of Ganga Residency:",
    )
    html = html.replace(
        "Spacious Villa Plots:",
        "Spacious Residential Plots:",
    )
    html = html.replace(
        "Choose from a variety of plot sizes to suit your lifestyle and preferences.",
        "Choose from 100 and 150 Sq.Yd. plot sizes in a 15 acre plotted township.",
    )
    html = html.replace(
        "Welcome to Ganga Residency, an exclusive residential project offering premium villa plots for sale in the serene town of Garhmukteshwar.",
        "Welcome to Ganga Residency, an upcoming 15 acre plotted township offering premium residential plots in the serene town of Garhmukteshwar.",
    )
    html = html.replace(
        "Welcome to Ganga Residency, an exclusive residential project offering premium villa\n                                        plots for sale in the serene town of Garhmukteshwar.",
        "Welcome to Ganga Residency, an upcoming 15 acre plotted township offering premium residential plots in the serene town of Garhmukteshwar.",
    )
    html = html.replace("Ganga Residency Master Plans", "Ganga Residency Master Plan")
    html = html.replace(
        "Ganga Residency offers a thoughtfully designed Vastu-friendly layout plan",
        "Ganga Residency offers a thoughtfully planned layout with 25 ft and 30 ft internal roads, green open spaces, and one tree planted in front of every plot",
    )
    html = html.replace(
        '<a href="assets/images/Ganga-Residency-Brochure.pdf" target="_blank" class="theme-btn style-one">Download Broucher',
        '<a href="contact.html" class="theme-btn style-one">Enquire Now',
    )
    html = html.replace("gc-popup", "gr-popup")
    html = html.replace("gc-location", "gr-location")
    html = html.replace("gc-price", "gr-price")
    html = html.replace("gc-popup-body", "gr-popup-body")
    html = html.replace("gc-submit-btn", "gr-submit-btn")
    html = html.replace(
        '<img src="assets/images/home-one/logo/logo-main.png" alt="Ganga Residency">',
        '<span class="brand-logo-text">Ganga Residency</span>',
    )
    html = html.replace(
        "Get More Details About ",
        "Get More Details About Ganga Residency",
    )
    html = html.replace(
        '"Ganga Residency offers excellent location',
        '"Ganga Residency offers an excellent location',
    )
    # Remove testimonial mentions if any county left - already replaced
    html = html.replace(
        '<section class="renvia-counter_three pt-115 pb-120"\n                    data-src="assets/images/home-three/bg/counter-bg.jpg">',
        '<section class="renvia-counter_three pt-115 pb-120" style="background: linear-gradient(135deg, #173b2c 0%, #1a4d38 100%);">',
    )
    html = html.replace(
        '<section class="renvia-make-sec bg_cover pt-120 pb-120"\n                    data-src="assets/images/home-three/bg/make-bg.jpg">',
        '<section class="renvia-make-sec bg_cover pt-120 pb-120" style="background: linear-gradient(135deg, #1C1C25 0%, #173b2c 100%);">',
    )
    html = html.replace(
        '<section class="renvia-choose-sec gray-bg pt-120 pb-120"\n                    data-src="assets/images/home-three/bg/choose-bg.jpg">',
        '<section class="renvia-choose-sec gray-bg pt-120 pb-120">',
    )
    # Highlights text updates on index
    highlights = [
        ("24-Hour Gated Security", "15 Acre Plotted Township"),
        ("5-Star Facilities Club House Society Park & Kids Play Area", "Luxury Clubhouse with premium lifestyle amenities"),
        ("Variety of stores in Shopping Complex", "All weather swimming pool & indoor badminton court"),
        ("Green Parks and Kids Play-Area", "Indoor games room, gym, library & restaurant"),
        ("Jogging Track/Yoga/Meditation Area", "Society internal roads: 25 ft & 30 ft wide"),
        ("2-Tier CCTV Security System", "1 tree with every plot (in front)"),
        ("Conveniently located near gas agencies, petrol pumps and police chowki", "Prime location in Garhmukteshwar with excellent connectivity"),
    ]
    for old, new in highlights:
        html = html.replace(f"<p>{old}</p>", f"<p>{new}</p>", 1)
    # Counter section - replace fake stats
    html = re.sub(
        r'<span class="title">Global Reach</span>\s*<h2><span class="counter">45</span><span class="symbol">\+</span>\s*</h2>\s*<p>Offices Worldwide</p>',
        '<span class="title">Plot Sizes</span><h2><span class="counter">100</span><span class="symbol">+</span></h2><p>Sq.Yd. Options</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<span class="title">Global Reach</span>\s*<h2><span class="counter">45</span><span class="symbol">\+</span>\s*</h2>\s*<p>Offices Worldwide</p>',
        '<span class="title">Pre-Launch Price</span><h2>₹<span class="counter">16500</span></h2><p>Per Sq.Yd.</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<span class="title">Global Reach</span>\s*<h2><span class="counter">45</span><span class="symbol">\+</span>\s*</h2>\s*<p>Offices Worldwide</p>',
        '<span class="title">Township</span><h2><span class="counter">15</span></h2><p>Acres</p>',
        html,
        count=1,
    )
    html = re.sub(
        r'<span class="title">Global Reach</span>\s*<h2><span class="counter">45</span><span class="symbol">\+</span>\s*</h2>\s*<p>Offices Worldwide</p>',
        '<span class="title">Road Width</span><h2><span class="counter">30</span><span class="symbol"> ft</span></h2><p>Internal Roads</p>',
        html,
        count=1,
    )
    html = html.replace(
        '<div class="shape"><img src="assets/images/home-three/gallery/make-shape1.png"\n                                    class="animate-float-bob-y" alt="shape"></div>',
        "",
    )
    return html


def add_popup_price_detail(html: str) -> str:
    if "gr-price-sub" in html:
        return html
    return html.replace(
        '<div class="gr-price">EFFECTIVE PRE-LAUNCH PRICE ₹16,500 / SQ.YD.</div>',
        '<div class="gr-price">EFFECTIVE PRE-LAUNCH PRICE ₹16,500 / SQ.YD.</div>\n                    <div class="gr-price-sub">Launch ₹17,500/Sq.Yd. | Save ₹1,000/Sq.Yd. Pre-Launch</div>',
    )


def process_file(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = replace_logo(html)
    html = remove_nav_items(html)
    html = add_residency_css(html)
    html = swap_project_images(html)
    html = update_content(html)

    if path.name == "index.html":
        html = replace_pricing_section(html)
        html = replace_amenities_slider(html)
        html = remove_sections(html)
        html = add_popup_price_detail(html)

    if path.name == "pricing.html":
        html = replace_pricing_section(html)

    path.write_text(html, encoding="utf-8")
    print(f"Updated {path.name}")


def main() -> None:
    for html_file in sorted(DOCS.glob("*.html")):
        process_file(html_file)


if __name__ == "__main__":
    main()
