describe("Butopea Cypress Tests", () => {

  it('checks for text and button', () => {
    cy.visit('https://butopea.com/');
    cy.get('.banner-square-overlay')
      .then(($banner) => {
        const text = $banner.find('.banner-square-overlay-heading p').text().trim();
        const buttonLabel = $banner.find('.banner-square-overlay-cta button').text().trim();
        assert.isNotEmpty(text);
        assert.isNotEmpty(buttonLabel);
        cy.log(`Title - ${text.trim}`);
        cy.log(`Button Lable - ${buttonLabel}`);
        cy.writeFile('results.txt', `--------Test 1 Details--------\nTitle - ${text}\nButton Lable - ${buttonLabel}\n--------Test Passed--------\n\n`);
      })
  });

  it('Retrieves image source URL', () => {
    cy.visit('https://butopea.com/')
    cy.get('.banner-square-column[style="order:3"]')
      .then(($block) => {
        const img_url = $block.find('img.block').attr('src');
        expect(img_url).to.not.be.empty;
        cy.log(`Image Url - https://butopea.com${img_url}`);
        cy.writeFile('results.txt', `--------Test 2 Details--------\nImage Link - https://butopea.com${img_url}\n--------Test Passed--------\n\n`, {
          flag: 'a+'
        });

      })
  });

  it('tests on New Products section', () => {
    cy.visit('https://butopea.com/');
    cy.get(':nth-child(3) > .secondary-font').click();
    cy.wait(5000);
    //I'm using for loop to log details of first 10 new products
    cy.writeFile('results.txt', `--------Test 3 Details--------\n`, {
      flag: 'a+'
    });
    for (let i = 1; i <= 10; i++) {
      cy.get(`:nth-child(${i}) > .product`)
        .then(($product) => {
          const title = $product.find('.product-tile-info p').text().trim();
          expect(title).to.not.be.empty;
          const product_link = $product.find('.product-link').attr('href');
          const price = $product.find('.lh30.cl-dark.weight-300.fs-medium-small').text().trim();
          const image_link = $product.find('.product-image__thumb').attr('src');
          cy.log(`Product ${i} details :`);
          cy.log(`Title - ${title}`);
          cy.log(`Product Link - https://butopea.com${product_link}`);
          cy.log(`Image Link - https://butopea.com${image_link}`);
          cy.log(`Price - ${price.replace('Ft','HUF')}`);
          cy.writeFile('results.txt', `Product ${i} details :\n`, {
            flag: 'a+'
          });
          cy.writeFile('results.txt', `Title - ${title}\n`, {
            flag: 'a+'
          });
          cy.writeFile('results.txt', `Product Link - https://butopea.com${product_link}\n`, {
            flag: 'a+'
          });
          cy.writeFile('results.txt', `Image Link - https://butopea.com${image_link}\n`, {
            flag: 'a+'
          });
          cy.writeFile('results.txt', `Price - ${price.replace('Ft','HUF')}\n\n`, {
            flag: 'a+'
          });
        })
    };
    cy.writeFile('results.txt', `\n--------Test Passed--------\n\n`, {
      flag: 'a+'
    });
  });
});