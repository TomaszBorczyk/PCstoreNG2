import { PCstoreNG2Page } from './app.po';

describe('pcstore-ng2 App', () => {
  let page: PCstoreNG2Page;

  beforeEach(() => {
    page = new PCstoreNG2Page();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
